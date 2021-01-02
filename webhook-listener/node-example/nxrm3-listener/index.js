
'use strict';
 
const express = require('express');
const bodyParser = require('body-parser');
// const { spawn } = require('child_process');

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
}));

const server = app.listen(3007, () => console.log('[NXRM3-Listener] webhook is listening'));

app.post('/', (req, res) => {
    console.log(req.body);
 
    const data = {
        responses: [
            {
                type: 'text',
                elements: ['Hi', 'Hello']
            }
        ]
    };
 
    // const child = spawn('ls -l /tmp', {
    //   detached: true,
    //   stdio: 'ignore'
    // });

    // child.unref();

    res.json(data);
});

