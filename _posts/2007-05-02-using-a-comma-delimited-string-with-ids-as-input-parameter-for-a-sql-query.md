---
layout: post
title: "Using a comma delimited string with id's as input parameter for a SQL query"
date: 2007-05-02T11:06:40.211000-07:00
tags: ["ASP.NET|Grid controls", "SQL Server", "T-SQL"]
author: "adminKris"
guid: "2a15f9d4-dd4d-4a98-b63e-10aa5241b83f"
published: true
comments: true
show_on_front: true
last_modified_at: 2007-05-02T11:29:43.758625-07:00
---

I just recently found out about a custom Split function for SQL Server 2000/2005 while I was reading this article: [Designing Reports with SQL Server Reporting Services 2005](/images/default.aspx "Reporting Services"). It mentioned a custom Split function made in T-SQL that could take in a delimited string with id's.

Today I had the need of such a functionality in my current project and luckely remembered where I saw it in the first place. Since I like it I thought I would create a small example for it. What it does is retrieve, from the Northwind database, some data of the Employees table and binds it to a GridView control. If you check several checkboxes and press the button you get, for those selected emloyees, to see everything that's in the database for them.

[Grab the Split function](/images/Default.aspx?level=root&file=procs.sql&url=http%3a%2f%2fmsdn.microsoft.com%2fmsdnmag%2fissues%2f06%2f06%2fDataPoints%2fdefault.aspx) from the article or get it here:

```
IF EXISTS (/images/
 SELECT * 
 FROM INFORMATION_SCHEMA.ROUTINES 
 WHERE SPECIFIC_NAME = N'Split' 
)
 DROP FUNCTION Split
GO
CREATE FUNCTION dbo.Split
(/images/
 @ItemList NVARCHAR(4000), 
 @delimiter CHAR(/images/1)
)
RETURNS @IDTable TABLE (/images/Item VARCHAR(50)) 
AS 

BEGIN 
 DECLARE @tempItemList NVARCHAR(/images/4000)
 SET @tempItemList = @ItemList

 DECLARE @i INT 
 DECLARE @Item NVARCHAR(/images/4000)

 SET @tempItemList = REPLACE (/images/@tempItemList, ' ', '')
 SET @i = CHARINDEX(/images/@delimiter, @tempItemList)

 WHILE (/images/LEN(@tempItemList) > 0)
 BEGIN
 IF @i = 0
 SET @Item = @tempItemList
 ELSE
 SET @Item = LEFT(/images/@tempItemList, @i - 1)
 INSERT INTO @IDTable(/images/Item) VALUES(/images/@Item)
 IF @i = 0
 SET @tempItemList = ''
 ELSE
 SET @tempItemList = RIGHT(/images/@tempItemList, LEN(@tempItemList) - @i)
 SET @i = CHARINDEX(/images/@delimiter, @tempItemList)
 END 
 RETURN
END 
GO
```

*All credits go the respective author of the formentioned article for making the function*.

I created the following stored procedure that makes use of the Split function:

```
CREATE PROCEDURE USP_RetrieveInformationForSelectedEmployees
 @p_selectedEmployees NVARCHAR(/images/50)
AS
BEGIN
 SELECT * 
 FROM Employees
 WHERE EmployeeID in (/images/SELECT Item FROM split(@p_selectedEmployees, ','))
END
```

And this is the ASP.NET webform:

```
 1: <%@ Page Language="C#" %>
```

```
 2: <%@ Import Namespace="System.Data.SqlClient" %>
```

```
 3: <%@ Import Namespace="System.Web.Configuration" %>
```

```
 4: <%@ Import Namespace="System.Data" %>
```

```
 5: 
```

```
 6: DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
```

```
 7: "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
```

```
 8: 
```

```
 9: <script runat="server">
```

```
 10: 
```

```
 11: protected void Button1_Click(/images/object sender, EventArgs e)
```

```
 12: {
```

```
 13: RetrieveInformationForSelectedEmployees();
```

```
 14: }
```

```
 15: 
```

```
 16: private void RetrieveInformationForSelectedEmployees()
```

```
 17: {
```

```
 18: StringBuilder sb = new StringBuilder();
```

```
 19: 
```

```
 20: // First loop through the GridView and see which
```

```
 21: // employees were selected. I use the StringBuilder
```

```
 22: // since the list could be a very long list.
```

```
 23: foreach (/images/GridViewRow row in GridView1.Rows)
```

```
 24: {
```

```
 25: if (/images/((CheckBox)row.FindControl("CheckBox1")).Checked)
```

```
 26: {
```

```
 27: sb.Append(/images/GridView1.DataKeys[row.RowIndex].Value.ToString() + ',');
```

```
 28: }
```

```
 29: }
```

```
 30: 
```

```
 31: using (/images/SqlConnection conn = new SqlConnection(WebConfigurationManager.ConnectionStrings
```

```
 32: ["NorthwindConnectionString"].ConnectionString))
```

```
 33: {
```

```
 34: using (/images/SqlCommand cmd = new SqlCommand("USP_RetrieveInformationForSelectedEmployees", conn))
```

```
 35: {
```

```
 36: cmd.CommandType = CommandType.StoredProcedure;
```

```
 37: cmd.Parameters.AddWithValue("@p_selectedEmployees", sb.ToString());
```

```
 38: 
```

```
 39: DataSet ds = new DataSet();
```

```
 40: SqlDataAdapter da = new SqlDataAdapter(/images/cmd);
```

```
 41: da.Fill(/images/ds);
```

```
 42: 
```

```
 43: GridViewResult.DataSource = ds;
```

```
 44: GridViewResult.DataBind();
```

```
 45: }
```

```
 46: }
```

```
 47: }
```

```
 48:
```

```
 49: script>
```

```
 50: 
```

```
 51: <html xmlns="http://www.w3.org/1999/xhtml" >
```

```
 52: <head runat="server">
```

```
 53: <title>Untitled Pagetitle>
```

```
 54: head>
```

```
 55: <body>
```

```
 56: <form id="form1" runat="server">
```

```
 57: <div>
```

```
 58: <asp:GridView ID="GridView1" runat="server" AutoGenerateColumns="False"
```

```
 59: DataKeyNames="EmployeeID" DataSourceID="SqlDataSource1">
```

```
 60: <Columns>
```

```
 61: <asp:TemplateField>
```

```
 62: <ItemTemplate>
```

```
 63: <asp:CheckBox ID="CheckBox1" runat="server" />
```

```
 64: ItemTemplate>
```

```
 65: asp:TemplateField>
```

```
 66: <asp:BoundField DataField="LastName" HeaderText="LastName"
```

```
 67: SortExpression="LastName" />
```

```
 68: <asp:BoundField DataField="FirstName" HeaderText="FirstName"
```

```
 69: SortExpression="FirstName" />
```

```
 70: <asp:BoundField DataField="Title" HeaderText="Title"
```

```
 71: SortExpression="Title" />
```

```
 72: Columns>
```

```
 73: asp:GridView>
```

```
 74: <asp:SqlDataSource ID="SqlDataSource1" runat="server"
```

```
 75: ConnectionString="<%$ ConnectionStrings:NorthwindConnectionString %>"
```

```
 76: SelectCommand="SELECT [EmployeeID], [LastName], [FirstName], [Title]
```

```
 77: FROM [Employees] ORDER BY [LastName], [FirstName]">
```

```
 78: asp:SqlDataSource>
```

```
 79:
```

```
 80: <asp:Button ID="Button1" runat="server" Text="Retrieve data" OnClick="Button1_Click" />
```

```
 81: <p>
```

```
 82: <asp:GridView runat="server" ID="GridViewResult" />
```

```
 83: p>
```

```
 84: div>
```

```
 85: form>
```

```
 86: body>
```

```
 87: html>
```




In lines 23 upto 29 I loop over the rows in the GridView and see if the checkbox in the first column was checked. If it was, I append the DataKey value of it to the StringBuilder instance. On line 37 I pass the string of all the selected employee IDs. The stored procedure uses the Split function in the IN clause.

Have fun!

Grz, Kris.

[![kick it on DotNetKicks.com](/images/UsingACommaDelimitedStringWithIdsAsInputParameterForASQLQuery.aspx)](/images/UsingACommaDelimitedStringWithIdsAsInputParameterForASQLQuery.aspx)

Technorati tags: [T-SQL](/images/T-SQL), [SQL Server](/images/SQL%20Server), [Function](/images/Function), [GridView](/images/GridView), [DataKey](/images/DataKey)
