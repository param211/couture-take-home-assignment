# Assignment
## Tasks:
* Implement JWT auth in FastAPI
* Use multithreading

## Solution
### Architecture
1. app/auth contains the files needed for jwt authentication
2. app/api.py contains the code for API endpoints and multithreading (and multiprocressing)

### Steps
1. run main.py to start the server
2. goto to `http://0.0.0.0:8081/docs`
3. use the UI to execute API requests

Note: `/multithreading` and `/multiprocessing` endpoints require authentication. The JWT token can be generated by creating a new user through `/user/signup`.