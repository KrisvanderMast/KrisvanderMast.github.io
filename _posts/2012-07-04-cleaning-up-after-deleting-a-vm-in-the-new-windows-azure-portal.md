---
layout: post
title: "Cleaning up after deleting a VM in the new Windows Azure portal"
date: 2012-07-04T14:28:37.735797-04:00
tags: ["Errormessages", "Storage", "WindowsAzure"]
author: "adminKris"
guid: "373fddd4-fa1c-4943-b2aa-bf9dcb215d47"
published: true
comments: true
show_on_front: true
last_modified_at: 2012-07-04T14:28:37.735797-04:00
---

When deleting a VM from your Windows Azure account as you might not need it anymore and you want to cut down on costs you can simply navigate to the portal, select the VM and press the Delete icon at the bottom:

[![storagedeletionerror01](/images/storagedeletionerror01_thumb.png "storagedeletionerror01")](/images/storagedeletionerror01_2.png)

That’s only the VM but when I set it up initially I chose to have a the Storage account to be auto generated. As a good housekeeper I didn’t only want to delete the VM but also the associated Storage as that might also still incur costs which I don’t want.

However when I tried to do so I got the following:

[![storagedeletionerror02](/images/storagedeletionerror02_thumb.png "storagedeletionerror02")](/images/storagedeletionerror02_2.png)

Clicking the i for more information it gave me the following error message:

**Storage account portalvhds0xgvcb5chg1gf has 1 container(/images/s) which have an active image and/or disk artifacts. Ensure those artifacts are removed from the image repository before deleting this storage account.**

Descriptive, but not really showing what I needed. It turned out to be that there’s also still a disk attached to the VM, but there was no indication in the portal that there was still something lying around. Simply navigating to **Virtual Machines** > **Disks** showed the associated disk:

[![storagedeletionerror03](/images/storagedeletionerror03_thumb.png "storagedeletionerror03")](/images/storagedeletionerror03_2.png)

Deleting this one and then going to the storage overview again I could delete the extra storage without problems:

[![storagedeletionerror04](/images/storagedeletionerror04_thumb.png "storagedeletionerror04")](/images/storagedeletionerror04_2.png)

I gave this back as feedback to the people at Microsoft and apparently it was listed as a bug but not yet taken care off. I’m sure it’ll be ironed out soon but in the mean time you can simply follow this little check to make sure you don’t have to pay extra costs when deleting a VM in total.

Grz, Kris.
