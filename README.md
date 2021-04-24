# CS 370 - Mobile Architecture & Programming

- Briefly summarize the requirements and goals of the app you developed. What user needs was this app designed to address?

    **The goal of the application developed was to create an easy-to-use interface for users who wish to record and track their weight. More specifically, a user needs to be able to use the application to record any number of weights they wish to record, add a goal weight, and receive a text message notification if and when they reach that goal.**

- What screens and features were necessary to support user needs and produce a user-centered UI for the app? How did your UI designs keep users in mind? Why were your designs successful?

    **The screens needed to support the user needs to include a login/sign up screen where users could enter their credentials to log in if they have an account, or sign up if they don't, a screen that displays all the weights the user has currently entered and gives them the option to perform CRUD actions on the weights, and a screen that lets the user add a goal weight if they so choose. My main focus during development was to ensure design elements were clear in their purpose, and that any button or text input was displayed in a logical and easy to understand manner.**

- How did you approach the process of coding your app? What techniques or strategies did you use? How could those be applied in the future?

    **I approached developing this application by breaking the project into sections. The first section I focused on was the database. I started coding the project by setting up the database schema and the supporting ORM classes that were needed. Then, I focused on filling in the functionality of the app by starting with the first screen a user would see, and working my way through the application flow. This same approach may not always apply to future projects, but I can most likely use the approach of breaking apart the requirements into small, workable pieces in the future.**

- How did you test to ensure your code was functional? Why is this process important and what did it reveal?

    **Each time I added a new functional component, I would run the Android emulated to ensure it was working as I had intended. It was important to do these for every new design element added to limit potential errors. There were often cases where I would find there was a null check missing or that I coded a logic error because I could notice the Android emulator would either not work like I had planned or completely crash.**

- Considering the full app design and development process, from initial planning to finalization, where did you have to innovate to overcome a challenge?

    **The part of my design that sticks out the most to me is the dynamic creation and deletion of views based on database rows. I needed to come up with a way for a user to be able to create, add, update, and delete weights within the application. I decided to provide a "DELETE" button in the table in order to support this, and I did so by dynamically allocating views to the TableLayout. This took some additional research on my part to get the exact layout I had designed previously and it came out just like I had hoped.**

- In what specific component from your mobile app were you particularly successful in demonstrating your knowledge, skills, and experience?

    **In designing the database schema. I was thorough in ensuring I was creating the proper indexes, trying to normalize the schema, and assigning foreign keys appropriately as I was developing.**