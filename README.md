0x00. AirBnB clone - The console
![AirBnb Logo](https://www.digital.ink/wp-content/uploads/airbnb_logo_detail.jpg)
Background Context
Welcome to the AirBnB clone project!

Before starting, please read the AirBnB concept page.
First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

    put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
    create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
    create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
    create the first abstracted storage engine of the project: File storage.
    create all unittests to validate all our classes and storage engine
Description of the command interpreter:

The interface of the application is just like the Bash shell except that this has a limited number of accepted commands that were solely defined for the purposes of the usage of the AirBnB website.

This command line interpreter serves as the frontend of the web app where users can interact with the backend which was developed with python OOP programming.

Some of the commands available are:

    show
    create
    update
    destroy
    count

And as part of the implementation of the command line interpreter coupled with the backend and file storage system, the folowing actions can be performed:

    Creating new objects (ex: a new User or a new Place)
    Retrieving an object from a file, a database etc…
    Doing operations on objects (count, compute stats, etc…)
    Updating attributes of an object
    Destroying an object

How to start it

These instructions will get you a copy of the project up and running on your local machine (Linux distro) for development and testing purposes.
Installing

You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.
