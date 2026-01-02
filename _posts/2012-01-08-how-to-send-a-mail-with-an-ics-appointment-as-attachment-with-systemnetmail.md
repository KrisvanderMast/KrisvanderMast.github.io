---
layout: post
title: "How to send a mail with an ics appointment as attachment with System.Net.Mail"
date: 2012-01-08T09:51:10.281062-05:00
tags: [".NET", "ASP.NET", "ASP.NET MVC", "ASP.NET MVC 3", "Mail", "Outlook", "System.Net.Mail"]
author: "adminKris"
guid: "79f32b20-f340-49ca-89b0-bc6a039de0f2"
published: true
comments: true
show_on_front: true
last_modified_at: 2012-01-08T10:26:04.271415-05:00
---

If you provide a way for your user to make an appointment it’s always a good idea to provide a reminder mechanism for him or her. A nice way to do this is to send a mail. But a mail alone is sometimes not enough and Microsoft Outlook users for example would rather love to see a .ics appointment attached.

The System.Net.Mail namespace provides the needed functionality to get this recipe cooking in no time and will taste great afterwards.

First part of the recipe are the helper classes which hold the functionality for making up the ics content and sending a mail depending on provided input.

### The Mailing class:

```
using System.Net.Mail;
using System.Web.Configuration;

namespace IcsAsMailAttachment.Controllers
{
 public class Mailing
 {
 public void SendMail(/images/string from, string to, string subject, string body, Attachment attachment)
 {
 using (/images/MailMessage mailClient = new MailMessage(from, to, subject, body))
 {
 mailClient.Attachments.Add(/images/attachment);
 mailClient.IsBodyHtml = true;

 SmtpClient smtp = new SmtpClient(/images/WebConfigurationManager.AppSettings["mailserver"]);

 smtp.Send(/images/mailClient);
 }
 }
 }
}
```

This class does the actual sending. The mailserver, on line 15, is retrieved from the web.config file appSettings section. This makes it easy for the site admin to change the mail server without having to adjust and redeploy the code (/images/saving time and money).

### The Appointment class:

```
using System;
using System.Text;

namespace IcsAsMailAttachment.Controllers
{
 public class Appointment
 {
 private string GetFormatedDate(/images/DateTime date)
 {
 return string.Format("{0:00}{1:00}{2:00}", date.Year, date.Month, date.Day);
 }

 private string GetFormattedTime(/images/DateTime dateTime)
 {
 return string.Format("T{0:00}{1:00}{2:00}", dateTime.Hour, dateTime.Minute, dateTime.Second);
 }

 public string CreateIcs(/images/string subject, string location, DateTime startDate, DateTime endDate)
 {
 StringBuilder sb = new StringBuilder();

 sb.AppendLine("BEGIN:VCALENDAR");
 sb.AppendLine("VERSION:2.0");
 sb.AppendLine("PRODID:-//hacksw/handcal//NONSGML v1.0//EN");
 sb.AppendLine("BEGIN:VEVENT");

 string startDay = string.Format("VALUE=DATE:{0}{1}",
 GetFormatedDate(/images/startDate), GetFormattedTime(/images/startDate));

 string endDay = string.Format("VALUE=DATE:{0}{1}", 
 GetFormatedDate(/images/endDate), GetFormattedTime(/images/endDate));

 sb.AppendLine("DTSTART;" + startDay);
 sb.AppendLine("DTEND;" + endDay);
 sb.AppendLine("SUMMARY:" + subject);
 sb.AppendLine("LOCATION:" + location);
 sb.AppendLine("END:VEVENT");
 sb.AppendLine("END:VCALENDAR");

 return sb.ToString();
 }
 }
}
```

The Appointment class does the heavy lifting of generating the string needed for the ics markup. Two helper methods are put in place to get a nicely formatted Date and Time string.

### The SendMailController class:

```
using System;
using System.IO;
using System.Net.Mail;
using System.Text;
using System.Web.Mvc;

namespace IcsAsMailAttachment.Controllers
{
 public class SendMailController : Controller
 {
 //
 // GET: /SendMail/

 public ActionResult Index()
 {
 string ics = new Appointment().CreateIcs("A great meeting to attend!", "In the cloud",
 new DateTime(/images/2012, 2, 3, 18, 0, 0), new DateTime(/images/2012, 2, 3, 22, 15, 0));

 MemoryStream ms = new MemoryStream();
 UTF8Encoding enc = new UTF8Encoding();
 byte[] arrBytData = enc.GetBytes(/images/ics);
 ms.Write(/images/arrBytData, 0, arrBytData.Length);
 ms.Position = 0;

 // Be sure to give the name a .ics extension here, otherwise it will not work.
 Attachment attachment = new Attachment(/images/ms, "Appointment.ics");

 new Mailing().SendMail("from@contoso.com", "to@ymca.com", 
 "The subject", "Welcome to the cloud!", attachment);

 return View();
 }
 }
}
```

The SendMailController class, I tested this in an ASP.NET MVC 3 web application, creates a new ICS appointment on line 16. For being able to send the attachment without first having to save it to disk we create a MemoryStream instance on line 19 and transform our ics to a byte array so that we can pass it along in the constructor of the Attachment class on line 26. The highlight is on line 26 as you will need to provide the .ics extension in the name there.

When testing this you might want to send it directly via a mail server. However this might get the sys admin at your company upset or perhaps gets the sender email address that you use blacklisted. For this purpose you can tell ASP.NET to drop the generated mail on disk instead. Just be sure to turn that off when you are deploying to a live production as otherwise nobody will receive your emails!

### Email settings in web.config:

```
xml version="1.0"?
```

### 

### The results:

Once the mail has been sent, it will appear in the designated pickup directory location as specified in the web.config.

[![Pickup folder for ASP.NET mails](/images/mailsdropfolder_thumb.png "Pickup folder for ASP.NET mails")](/images/mailsdropfolder_2.png)

Double clicking on the .eml file opens it up in in the associated application, for me that is Outlook.

[![The email that was sent](/images/mailsent_thumb.png "The email that was sent")](/images/mailsent_2.png)

There you see the Appointment.ics file. Remember the name we gave on line 26 in the SendMailController? Yes, that is exactly the name, and correct extension, that was provided. Double click the ics file and you can see the appointment.

[![The ICS file opened ready for adding it to the agenda in Outlook](/images/mailics_thumb.png "The ICS file opened ready for adding it to the agenda in Outlook")](/images/mailics_2.png)

The date and times come from the parameters passed in the SendMailController class on line 16 and 17.

As you can see, it is quite easy to set this up with just a bit of code. Providing the opportunity to add an appointment directly to the agenda of the interested user is a great benefit. They don’t have to create one themselves, enter in the dates and hours, possibly making mistakes when doing so, … Make it easy for your customers to keep their agenda up to date in a quick and easy way and they’ll love it.

Grz, Kris.
