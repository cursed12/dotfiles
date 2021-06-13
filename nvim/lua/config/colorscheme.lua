local utils = require('utils')
local cmd = vim.cmd

-- Set colorscheme and transparent background
utils.opt('o', 'termguicolors', true)
--cmd 'let ayucolor="dark"'
cmd 'colorscheme dracula'
cmd 'highlight Normal guibg=none'
cmd 'highlight LineNr guifg=grey'

-- Enable italics if available
--vim.g.onedark_terminal_italics = 1

