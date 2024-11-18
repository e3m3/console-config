--  CodeCompanion plugin spec
--  From `https://github.com/olimorris/codecompanion.nvim?tab=readme-ov-file#package-installation`

local table_cc = {
  "olimorris/codecompanion.nvim",
  dependencies = {
    "nvim-lua/plenary.nvim",
    "nvim-treesitter/nvim-treesitter",
    "hrsh7th/nvim-cmp", -- Optional: For using slash commands and variables in the chat buffer
    "nvim-telescope/telescope.nvim", -- Optional: For using slash commands
    { "MeanderingProgrammer/render-markdown.nvim", ft = { "markdown", "codecompanion" } }, -- Optional: For prettier markdown rendering
    { "stevearc/dressing.nvim", opts = {} }, -- Optional: Improves `vim.ui.select`
  },
  config = function()
    require("codecompanion").setup({
      adapters = {
        codellama = function()
          return require("codecompanion.adapters").extend("ollama", {
            name = "codellama", -- Give this adapter a different name to differentiate it from the default ollama adapter
            schema = {
              model = {
                default = "codellama:7b",
              },
              num_ctx = {
                default = 256,
              },
              num_predict = {
                default = -1,
              },
            },
            env = {
              url = "http://localhost:11434",
              -- api_key = "OLLAMA_API_KEY",
            },
            headers = {
              ["Content-Type"] = "application/json",
              -- ["Authorization"] = "Bearer ${api_key}",
            },
            parameters = {
              sync = true,
            },
          })
        end,
      },
      strategies = {
        chat = {
          adapter = "codellama",
        },
        inline = {
          adapter = "codellama",
        },
        agent = {
          adapter = "codellama",
        },
      },
      display = {
        chat = {
          window = {
            layout = "horizontal", -- float|vertical|horizontal|buffer
          },
        },
      },
    })
  end,
  init = function() end,
}

vim.api.nvim_set_keymap("n", "<C-k>", "<cmd>CodeCompanionActions<cr>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("v", "<C-k>", "<cmd>CodeCompanionActions<cr>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("n", "<LocalLeader>k", "<cmd>CodeCompanionChat Toggle<cr>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("v", "<LocalLeader>k", "<cmd>CodeCompanionChat Toggle<cr>", { noremap = true, silent = true })
vim.api.nvim_set_keymap("v", "gk", "<cmd>CodeCompanionChat Add<cr>", { noremap = true, silent = true })

--  Expand 'cc' into 'CodeCompanion' in the command line
vim.cmd([[cab cc CodeCompanion]])

return table_cc
