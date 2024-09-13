-- .vimrc file

vim.api.nvim_command("filetype plugin on")
vim.api.nvim_command("filetype indent on")
vim.api.nvim_command("syntax on")
vim.api.nvim_command("set mouse=a")

vim.o.autoread = true

vim.o.ruler = true
vim.o.showcmd = true
vim.o.background = dark

vim.o.incsearch = true
vim.o.ignorecase = true
vim.o.smartcase = true

vim.o.number = true
vim.o.numberwidth = 3

vim.o.shiftwidth = 4
vim.o.tabstop = 4
vim.o.softtabstop = 4
vim.o.expandtab = true
vim.o.smarttab = true

vim.o.splitright = true
vim.o.splitbelow = true

vim.o.autoindent = true
vim.o.copyindent = true

vim.o.wrap = true
vim.o.linebreak = true

vim.o.incsearch = true
vim.o.hlsearch = true

vim.api.nvim_command("au! BufRead,BufNewFile *.ll     set filetype=llvm")
vim.api.nvim_command("au! BufRead,BufNewFile *.llvm   set filetype=llvm")
