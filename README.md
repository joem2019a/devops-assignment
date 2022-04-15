# IT Asset Manager

To run you need Python3, Pip3, NodeJS and NPM installed.

Install dependencies:
```
pip3 install -r api/requirements.txt
cd ui
npm install
cd ..
```

Open two terminals and run the following:
```
# terminal 1
cd api
python3 app.py

# terminal 2
cd ui
npm start
```

Open [http://localhost:3000](http://localhost:3000).

Create a user with 'admin' somewhere in the username to make a user with administrator privilages. This vulnerability is for demonstration purposes.
