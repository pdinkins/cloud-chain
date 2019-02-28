const { BrowserWindow } = require('electron')

let win = new BrowserWindow({ width: 800, height: 600 })
win.on('closed', () => {
    win = null
})

win.loadURL('http://127.0.0.1:6419/')