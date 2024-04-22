# InferGPT: your local personalised AI agent

InferGPT's mission is to be an AI that knows you better than your best friend. A system that personalises to who you are and what you care about. We want to build something that can:

🔗 Ingest data about you from various sources (with your permission of course)  
💡 Have deep and personal conversations without having to answer lots of questions - it will already infer your needs, make personalised recommendations and remember all your conversations.  
🎯 Help you set and keep track of goals.  
🏗️ Carry out tasks: this is an agent after all - it will go away and action stuff for you!  
🔮 Predict what you need before you need it!  

We aim to be able to answer complex questions that require a deep understanding of someone to effectively answer, such as:
1) How can i be better with my finances?
2) I'm trying to lose weight but its not working, why? 
3) I'm learning to code, can you create a tailored learning plan?  

## Roadmap & Docs
Want more context about how it works, our roadmap and documentation? Check out the [wiki](https://github.com/WaitThatShouldntWork/InferGPT/wiki)

For further reading on InferGPT's components, see any of the following
- [Full system testing](test/README.md)
- [Data persistence](data/README.md)
- [Backend](backend/README.md)
- [Frontend](frontend/README.md)
- [Assets](assets/README.md)
- [Testing](test/README.md)
- [Financial Bot](financialhealthcheckScottLogic/README.md)

## Contribute
See [the contribution guide](CONTRIBUTING.md) for further guidance. Note this guide is in progress!

## Getting Started

In the top-right corner of the page, click Fork.

On the next page, select your GitHub account to create the fork under.
Wait for the forking process to complete. You now have a copy of the repository in your GitHub account.

### Clone the Repository

To clone the repository, you need to have Git installed on your system. Use the [official Git installer](https://git-scm.com/download/win) or [follow the terminal commands guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

Once you have Git installed, follow these steps:

- Open your terminal.
- Navigate to the directory where you want to clone the repository.
- Run the git clone command for the fork you just created.

### Install Neo4j Desktop or Aura DB
Instructions can be found [here](https://neo4j.com/docs/?utm_medium=PaidSearch&utm_source=google&utm_campaign=GDB&utm_content=EMEA-X-Conversion-GDB-Text&utm_term=neo4j&gclid=Cj0KCQiA1rSsBhDHARIsANB4EJY8wQONKSyNCofQBGAcOGWwNpNh4Z0yj7oGxok8vs2CipPJMjGPcpkaAuw1EALw_wcB).  
Install the pre-made recommendations database. Version 4.4 is the latest stable.

### Running the service
- Create `.env` files based on the `.env.example` files under `/frontend` and `/backend`

#### Using Docker
- Start and open the Neo4J Desktop app. Start the default database (neo4j).
- create `.env` files as instructed within the [frontend README](frontend/README.md) and [backend README](backend/README.md)
- Run the Docker Desktop app (install it from [docker.com](docker.com) if you don't have it)
- In the root directory of the project run `docker compose up`
  - Note the first time you do this it may take longer as the compose file builds the images
  - to delete and recreate the images use
    - kill containers `docker rm $(docker ps -a -f status=exited -q)`
	  - kill images `docker rmi infergpt-backend infergpt-frontend`
	  - restart `docker compose up`

#### Using pip and python
- Open your preferred terminal.
It's recommended (though not technically required) to create a virtual environment for the project by running `python -m venv .venv` to create it and `.venv/Scripts/activate` to activate it in your active terminal.
- Follow the [frontend README](frontend/README.md) to set up the front end
- Follow the [backend README](backend/README.md) to set up the back end
- Once all dependencies have been pulled run `uvicorn app:api` to start the app. Check the backend app is running at [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health).
 
### Usage
Coming

### LICENCE
See [LICENCE.md](LICENCE.md)
