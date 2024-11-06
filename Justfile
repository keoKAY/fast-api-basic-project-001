run app: 
    #!/bin/bash
    echo "Starting the program on the port :8080 " 
    uvicorn app.main:app --reload --port 8080