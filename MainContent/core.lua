decisions = {}
scopes = {}

function createDecision(table)
    defaults = {
        id = "id",
        allowed = function() return true end,
        visible = function() return true end,
        available = function() return true end,
        effects = function() return true end,
        timeout = 1,
        fire_only_once = false
    }
    for key, value in pairs(defaults) do
        if table[key] == nil then
            table[key] = value
        end
    end
    decisions[table.id] = table;
end