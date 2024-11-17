--  Setup codecompanion plugin
--  From `https://github.com/olimorris/codecompanion.nvim?tab=readme-ov-file#electric_plug-adapters`

require("codecompanion").setup({
  adapters = {
    ollama = function()
      return require("codecompanion.adapters").extend("ollama", {
        env = {
          url = "https://localhost:11434",
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
})
