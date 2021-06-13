-- Some basic utility keymaps
local utils = require('utils')

-- Leader
vim.g.mapleader = ' '

-- Save File
utils.map('n', '<C-S>', ':w<CR>')

-- Remapping to Escape the Escape key
utils.map('i', 'jk', '<Esc>')
utils.map('v', 'jk', '<Esc>')

-- Terminal commands
utils.map('n', '<Leader>tt', ':new +resize17 term://bash<CR>')
utils.map('t', 'jk', '<C-\\><C-N>')

-- File tree toggle
utils.map('n', '<Leader>e', ':NERDTreeToggle<CR>')

-- Open and source init.lua from anywhere inside Vim
utils.map('n', '<Leader>so', ':luafile ~/.config/nvim/init.lua<CR>')
utils.map('n', '<Leader>vc', ':cd ~/.config/nvim/<CR>:NERDTreeCWD<CR>')

-- Jump thru splits like a ninja
utils.map('n', '<C-J>', '<C-W><C-J>')
utils.map('n', '<C-K>', '<C-W><C-K>')
utils.map('n', '<C-L>', '<C-W><C-L>')
utils.map('n', '<C-H>', '<C-W><C-H>')

-- Remove highlighted searches
utils.map('n', '<Leader>hl', ':set nohlsearch<CR>')

--Zoom thru buffers voohoooo
utils.map('n', '<Leader>bn', ':bn<CR>')
utils.map('n', '<Leader>nb', ':bp<CR>')
utils.map('n', '<Leader>b', ':buffers<CR>:buffer<Space>')

--Nerd Tree change dir to pwd
utils.map('n', '<Leader>cd', ':NERDTreeCWD<CR>')

--Break free outta brackets
utils.map('i', '<C-L>', '<Right>')
