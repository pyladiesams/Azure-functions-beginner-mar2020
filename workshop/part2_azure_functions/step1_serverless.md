### Step 1: Getting familiar with the Cloud & Serverless.

## Short introduction to Serverless Architecture

Serverless architecture (also known as serverless computing or function as a service (FaaS)) is a cloud computing execution model where the cloud 
provider dynamically manages the allocation and provisioning of servers, eliminating the need for server management by the developer.

It's important to note that Serverless architecture does not mean no server. Your code still runs on a server, but you don’t have to care about the 
underlying infrastructure because a third-party service will handle it for you. This leads to less time in operations and more time for developing software!
 
With Serverless you compose your application into individual, event-triggered, autonomous functions. 
Each function is hosted by the cloud provider and can be scaled automatically in real-time based on computing needs. 
This turns out to be very cost effective. For example, your app can automatically scale during peak hours and shut down the additional resources when you no longer need them.  

Serverless architecture is especially beneficial if you have a small number of functions that you need to host. If your application is more complex, 
a Serverless architecture can still be beneficial, but you might need to refactore your code and over time migrate small pieces of your application 
into Serverless functions. 

Now that we have basic understanding of what a Serveless architecture is let's take a look into one of the cloud providers [Microsoft Azure](https://azure.microsoft.com/).

According to their web-site:
>> Azure is an ever-expanding set of cloud computing services to help your organization meet its business challenges. Azure gives you the freedom to 
build, manage, and deploy applications on a massive, global network using your preferred tools and frameworks.

Azure Functions is Azure’s event-driven serverless compute platform. They were introduced to provide simplified and scalable way of developing event-driven solutions.

In 2019 Azure Functions introduced Python support. Python is a great fit for data manipulation, machine learning, scripting, and automation scenarios. 
Building these solutions using Azure Functions can take away the burden of managing the underlying infrastructure, so you can move fast and build, test, and deploy your
code to the end user in a much easier way.

In the next step, let's dive deeper in Azure Functions!


## Want to learn more about Serverless?

* https://docs.microsoft.com/en-gb/azure/guides/developer/azure-developer-guide
* https://docs.microsoft.com/en-gb/learn/
* https://read.acloud.guru/

