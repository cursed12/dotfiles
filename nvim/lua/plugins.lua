local execute = vim.api.nvim_command
local fn = vim.fn

local install_path = fn.stdpath('data')..'/site/pack/packer/start/packer.nvim'

if fn.empty(fn.glob(install_path)) > 0 then
  fn.system({'git', 'clone', 'https://github.com/wbthomason/packer.nvim', install_path})
  execute 'packadd packer.nvim'
end


-- This file can be loaded by calling `lua require('plugins')` from your init.vim

return require('packer').startup(function()
     
    -- Packer can manage itself
    use 'wbthomason/packer.nvim'

    -- File tree
    use {
	'preservim/nerdtree',
	requires = {'ryanoasis/vim-devicons'}
	}

    -- Complete brackets
    use 'jiangmiao/auto-pairs'
  
    -- Colorscheme(s)
    use 'gruvbox-community/gruvbox'
    use 'dracula/vim'
    use 'ayu-theme/ayu-vim'

    -- A good statusline
    use {
	'vim-airline/vim-airline',
    	'vim-airline/vim-airline-themes'
	}

    -- The only Fuzzy finder you'll ever need
    use {
        'nvim-telescope/telescope.nvim',
        requires = {{'nvim-lua/popup.nvim'}, {'nvim-lua/plenary.nvim'}}
    }
    
    --Easily comment lines and blocks
    use 'preservim/nerdcommenter'

    --A nice philosophical startup screen
    use 'mhinz/vim-startify'

    --Autocompletion with Native LSP for the grassfed coconut oil experience
    use {   'neovim/nvim-lspconfig', 
            'hrsh7th/nvim-compe'
        }

    --Superior syntax highlighting
    use { 'nvim-treesitter/nvim-treesitter', run = ':TSUpdate' }

    -- Git integration
    use {
        'tpope/vim-fugitive',
        'mhinz/vim-signify'
    }

    -- Great colors
    use 'norcalli/nvim-colorizer.lua'

end)

