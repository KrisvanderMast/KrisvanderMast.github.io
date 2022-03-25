---
layout: post
title: Using SqlBulkCopy with .NET lists
date: 2022-03-23 09:52:11 +0200
comments: true
published: true
categories: ["post"]
tags: ["dotnet",".NET","SqlBulkCopy","EF Core,","Entity Framework"]
author: Kris van der Mast
---
Recently I was in a situation where I had to quickly inject loads of data into a [SQL database][1]. The basic setup of the application:

- Read a bunch of files
- Process the data in the files, extract valuable information, do calculations on them, ...
- Write the analyzed result into a table in SQL Server

Not the epically most difficult application out there. The second step took most of the time to write, test and check with business if the results were as expected (first time right btw).

Reading and processing about 40000 files took several minutes. Writing the results into into the database's table took longer. Considerably longer... like the application crashed after having sucked out all cpu and most of the memory of the laptop for 4.5 hours.

Ok, so what went wrong? It turned out to be that the processing and crunching of the data generated around 7 million records which I didn't expect when I ran the first real test scenario with 40000 files. As I had worked in the same application already with [Entity Framework][2] I reused that to insert all the processed data into the database. Which resulted into the crash ultimately as I got an updated exception. Which I still find a bit strange as everything was simply inserts of unique data. For the record, I didn't further investigate it as I wanted to get the application running.

So, back to the drawing table and [SqlBulkCopy][3] came on my radar first. From the documentation:

> Lets you efficiently bulk load a SQL Server table with data from another source.

Sounds like a good choice right? However the documentation quickly showed that there was going to be a little more work involved from my side:

| Method | Explanation |
|-|-|
|WriteToServer(DataTable, DataRowState)| Copies only rows that match the supplied row state in the supplied DataTable to a destination table specified by the DestinationTableName property of the SqlBulkCopy object. |
|WriteToServer(IDataReader)|Copies all rows in the supplied IDataReader to a destination table specified by the DestinationTableName property of the SqlBulkCopy object.|
|WriteToServer(DataTable)|Copies all rows in the supplied DataTable to a destination table specified by the DestinationTableName property of the SqlBulkCopy object.|
|WriteToServer(DbDataReader)|Copies all rows from the supplied DbDataReader array to a destination table specified by the DestinationTableName property of the SqlBulkCopy object.|
|WriteToServer(DataRow[])|Copies all rows from the supplied DataRow array to a destination table specified by the DestinationTableName property of the SqlBulkCopy object.|

None of these fit the custom classes with `List<T>` I was using in my C# code. I could come up with something myself and write some small piece of code to convert things around and make it work, or, I could look around what's already out there that would do the job for me...

A quick search on [StackOverflow][4] gave code samples made by people who clearly hit the same situation I was in. One solution made use of [fast-member][5]. Looking into the readme of the project gave the indication that it might indeed be a good approach.

The method I came up with was the following:

```csharp
void BulkCopyIntoAnalysisResult(IEnumerable<AnalysisResult> a)
{
    using var bcp = new SqlBulkCopy(connectionString);
    using var reader = ObjectReader.Create(a, nameof(AnalysisResult.Id), 
        nameof(AnalysisResult.RunId), nameof(AnalysisResult.FoundInFiles),
        nameof(AnalysisResult.CardIsKnownToUs), nameof(AnalysisResult.FoundInformationOnPosition), 
        nameof(AnalysisResult.Card),
        nameof(AnalysisResult.EmployerNumber), nameof(AnalysisResult.EmployeeNumber), nameof(AnalysisResult.Count), 
        nameof(AnalysisResult.CreatedOn));

    bcp.DestinationTableName = nameof(AnalysisResult);
    bcp.BulkCopyTimeout = 8 * 60 * 60;
    bcp.WriteToServer(reader);
}
```

where `AnalysisResult` is a custom class that holds the endresult of all the data crunching. The destination table was generated with [EF Migrations][6] based on that class.

After this _upgrade/refactor/improvement_ running the application gave way better results. Storing the data took a couple of minutes while memory and cpu were not really stressed out like with the first approach.

Hopefully you found it an interesting read and can (re)use this approach to improve your bulk inserting of data as well.

While we're at it, I'm getting thirsty and you might want to 

<a href="https://www.buymeacoffee.com/KrisvanderMast" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

[1]: https://www.microsoft.com/en-us/sql-server/sql-server-downloads
[2]: https://docs.microsoft.com/en-us/ef/
[3]: https://docs.microsoft.com/en-us/dotnet/api/system.data.sqlclient.sqlbulkcopy?view=dotnet-plat-ext-6.0
[4]: https://www.stackoverflow.com/
[5]: https://github.com/mgravell/fast-member
[6]: https://docs.microsoft.com/en-us/ef/core/managing-schemas/migrations/?tabs=dotnet-core-cli
