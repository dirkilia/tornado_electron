const electron = require("electron");
const { app, BrowserWindow } = require('electron')

let win;

function createWindow() {
    win = new BrowserWindow({
        width: 700,
        height: 500
    })

    win.loadFile('index.html')

    win.on('closed', () => {
        win = null;
    })
}

app.on('ready', createWindow)

app.on('window-all-closed', () => {
    app.quit();
})
