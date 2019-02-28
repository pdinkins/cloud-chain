const { BrowserWindow } = require('electron')

let win = new BrowserWindow({ width: 800, height: 600 })
win.on('closed', () => {
    win = null
})

win.loadURL('http://localhost:6419/')