// Cloud Chain Electron Front End UI 

const { app, BrowserWindow } = require('electron')

let win

function createWindow () {
 
  win = new BrowserWindow({
      show: true,
      width: 1024,
      height: 768,
      minWidth: 400,
      minHeight: 200,
      resizable: true,
      center: true,
      autoHideMenuBar: true
  })
  // win.loadFile('index.html')
  // display grip md previewer
  win.loadURL('http://localhost:6419/')
  // win.webContents.openDevTools()
  win.on('closed', () => {
    win = null
  })
}

app.on('ready', createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (win === null) {
    createWindow()
  }
})
