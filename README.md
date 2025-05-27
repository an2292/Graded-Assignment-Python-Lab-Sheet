Assignment 1 - Python and SQL

The entrypoint to the application is `cli.py`, to run:

```
python cli.py
```

The CLI class handles user interaction and gets input from the user. The CLI class
interacts with the Client class which encapsulates methods for taking parameters (where appropriate)
from the user and safely passing them into SQL statements as parameters. The Database class
encapsulates database operations and also handles, starting and closing connections safely.
