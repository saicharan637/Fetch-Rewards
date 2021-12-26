### About the Exercise

This Web Service is built using Flask, which is a micro web framemework written in Python. I decided to use Flask because, it's perfect for building light weight web applications and also comes with a built in server, which is good enough for testing.

### Built With

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Python](https://www.python.org/)


### Installation

1. Download and Install the Latest Version of Python from here : [https://www.python.org/downloads/]

2. Clone the repo
   ```sh
   git clone https://github.com/saicharan637/Fetch-Rewards.git
   ```
3. Install Flask
   ```sh
   pip install flask
   ```
4. Install VS Code(Not Mandatory): [https://code.visualstudio.com/]

5. Install Postman for API testing(Not Mandatory): [https://www.postman.com/downloads/]

6. If you're using a Windows Operating System, check this link below on how to Install and Use Linux Bash Shell on Windows :
[https://www.howtogeek.com/249966/how-to-install-and-use-the-linux-bash-shell-on-windows-10/]

7. Alternatively, you can also download and install Git Bash to use Bash Shell:
[https://git-scm.com/downloads]


### Usage

1. Open a Text Editor/IDE and and navigate to the folder "Fetch Rewards" inside the repository. The Source Code for the Entire Exercise is contained in the file ``app.py``.

2. The Structure of the Folder is as belows:
```
├── Fetch Rewards                   
    ├── app.py                   
    ├── points.pdf
    ├── README.md
    ├── TestSuite.txt
```
2. If you're using VS Code, open the folder and open the built in terminal inside VS Code and enter the following commands:
```sh
   pip install flask
   ```
```sh
   python app.py
   ```
This starts a development server locally on the URL:
http://127.0.0.1:5000/.

3. Once the Server is up and running, navigate to the URL:
http://localhost:5000/ (or) http://127.0.0.1:5000/ and you should be able to see a Text Message saying: ```Welcome to Fetch Rewards Coding Exercise!```.
If you can see the above message, please proceed to the next steps, if not kill the server using ```ctrl+c``` and stop any processs running on port 5000 and restart the Flask Server by typing ```python app.py```.


## Testing

1. Once the server is up and running, we are now ready to test the web service. It is recommend to test the API using Postman or via a bash shell.

2. The Test Cases are provided in the file ```TestSuite.txt```.

3. We are using curl commands to transfer data to and from the server.

### There are two ways to Test the Web Service:

4. Open the TestSuite file and in Postman, go to File->Import->Raw text->paste the curl commands one at a time->continue->Import->Send, you can see the reponse of the request in the Reponse window.

5.  Open a Bash Shell and from the TestSuite file, copy and run the curl commands one at a time and the output is diplayed, once the command is executed.

6. The Balance can be checked after adding points and/or spending points.

### Assumptions:

1.  The points being spent are always greater than 0.

2.  The User has enough points available in their account to spend, if the user tries to spend more points than they have, an Error reponse saying "{ TotalPoints: "Points are available to Spend only!" } will be retuned, where "TotalPoints" are the total points available in User's account.