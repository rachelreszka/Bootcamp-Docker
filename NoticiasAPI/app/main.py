import uvicorn
 
if __name__ == "__main__":
 uvicorn.run("server.app:app", host="172.19.211.205", port=5000, reload=True)