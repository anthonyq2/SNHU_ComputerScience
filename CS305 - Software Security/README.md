# CS305 - Software Security

Briefly summarize your client, Artemis Financial, and their software requirements. Who was the client? What issue did they want you to address?

**The client, Artemis Financial, is a financial institution seeking to add a file verification step to their web application to secure communications. They needed to do this by adding a data verification step in the form of a checksum when the web application is used to transfer data.**

What did you do particularly well in identifying their software security vulnerabilities? Why is it important to code securely? What value does software security add to a company’s overall wellbeing?

**I think one thing I did well in identifying their software security vulnerabilities was understanding the issues that come with designing an application that communicates across the web. To make design decisions or this type of application, you need to understand the differences between encryption algorithms and the types of systems they are used for.**

What about the process of working through the vulnerability assessment did you find challenging or helpful?

**It was challenging to adapt to programming languages and frameworks I wasn't as familiar with. I am not a professional Java engineer, so being able to apply what I know about computer science in general to a programming language I don't know the ins and outs of was a challenge.**

How did you approach the need to increase layers of security? What techniques or strategies would you use in the future to assess vulnerabilities and determine mitigation techniques?

**The way I approached the need to increase layers of security was in steps. It makes a project much easier to handle if you tackle the vulnerability assessment in steps. For example, you can start by running a tool like dependency check to understand where immediate vulnerabilities might lie within the application. Once you do that, you can move to a manual review of the code to identify more security vulnerabilities that exist. I would take a similar approach in the future to assess vulnerabilities.**

How did you ensure the code and software application were functional and secure? After refactoring code, how did you check to see whether you introduced new vulnerabilities?

**After refactoring, it's essential to run the same tests you did before refactoring. Running tools such as a dependency check can let you know whether any dependencies you added have known security vulnerabilities. Ideally, another step you would take to make sure your changes are secure would be to have your code reviewed by colleagues. For this class, this was not a requirement, so that step did not take place.**

What resources, tools, or coding practices did you employ that you might find helpful in future assignments or tasks?

**I think the Java keytool is a tool I learned about from this class that I may be going back to in the future. The ability to quickly generate self-signed certs is particularly useful when doing development work.**

Employers sometimes ask for examples of work that you have completed to demonstrate your skills, knowledge, and experience. What from this particular assignment might you want to showcase to a future employer?

**From this assignment I might choose to showcase the implementation of SSL with Spring. Although this is not a particularly difficult server to configure, I think it's useful knowledge to understand how to secure a server with a cert.**
