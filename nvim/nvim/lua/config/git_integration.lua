local utils = require('utils')
local wo = vim.wo

utils.map('n', '<Leader>gs', ':Git<CR>')
utils.map('n', '<Leader>gc', ':Git commit<CR>')
utils.map('n', '<Leader>gp', ':Git push<CR>')

wo.signcolumn = 'yes'

vim.g.signify_sign_add               = '+'
vim.g.signify_sign_delete            = '_'
vim.g.signify_sign_delete_first_line = '‾'
vim.g.signify_sign_change            = '~'

