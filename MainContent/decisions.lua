createDecision({
    id = "Clear_Timeout",

    effects = function()
        CoI:ClearDecisionTimeout(scopes[#scopes], "Timeout_Long")
    end,

    timeout = 0
})
createDecision({
    id = "Timeout_Long",
    
    timeout = 1000
})
createDecision({
    id = "Become_Purple",

    allowed = function() 
        return CoI:OwnsTile(scopes[#scopes], "russia")
    end,

    effects = function()
        CoI:SetColor(scopes[#scopes], "purple")
    end,

    fire_only_once = true
})

print(decisions)