// Will need to fill this in every time the server restarts
// which is every four hours
// Alternatively, I can just run it from local MySQL
// instead of from AWS
// local fastapi runs on uvicorn on port 8000
// Argh! you have to put http:// in front of the localhost!
export const SERVER_PUBLIC_IP = 'http://localhost:8000'
