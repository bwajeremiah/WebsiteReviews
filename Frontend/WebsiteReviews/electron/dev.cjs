// Starts the Vite dev server, waits for it, then launches Electron against it.
// `electron .` on its own only opens a window - it does not run Vite.
const { spawn } = require('node:child_process')
const path = require('node:path')

const root = path.join(__dirname, '..')
const url = 'http://localhost:5173'

const vite = spawn(process.execPath, [path.join(root, 'node_modules', 'vite', 'bin', 'vite.js')], {
  cwd: root,
  stdio: 'inherit',
})

let electron = null
let shuttingDown = false

function shutdown(code = 0) {
  if (shuttingDown) return
  shuttingDown = true
  if (electron && !electron.killed) electron.kill()
  if (!vite.killed) vite.kill()
  process.exit(code)
}

async function waitForServer(timeoutMs = 30000) {
  const start = Date.now()
  while (Date.now() - start < timeoutMs) {
    try {
      const res = await fetch(url)
      if (res.ok) return true
    } catch {
      // server not up yet
    }
    await new Promise((resolve) => setTimeout(resolve, 250))
  }
  return false
}

vite.on('exit', (code) => {
  // Vite died (bad config, port in use, ...) - nothing to show in Electron.
  if (!shuttingDown) shutdown(code ?? 1)
})

;(async () => {
  const ready = await waitForServer()
  if (!ready) {
    console.error(`Vite dev server did not start at ${url}`)
    shutdown(1)
    return
  }

  const electronPath = require('electron')
  electron = spawn(electronPath, ['.'], {
    cwd: root,
    stdio: 'inherit',
    env: { ...process.env, ELECTRON_START_URL: url },
  })

  electron.on('close', (code) => shutdown(code ?? 0))
})()

process.on('SIGINT', () => shutdown(0))
process.on('SIGTERM', () => shutdown(0))
