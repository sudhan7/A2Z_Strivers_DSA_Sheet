def getWorkflowReplacements(config):
    MOD = 10**9 + 7
    digits = 10

    dp = [0] * digits

    # initialize first position
    if config[0] == '?':
        for d in range(digits):
            dp[d] = 1
    else:
        dp[int(config[0])] = 1

    for i in range(1, len(config)):
        new_dp = [0] * digits
        total = sum(dp) % MOD

        if config[i] == '?':
            for d in range(digits):
                new_dp[d] = (total - dp[d]) % MOD
        else:
            d = int(config[i])
            new_dp[d] = (total - dp[d]) % MOD

        dp = new_dp

    return sum(dp) % MOD

s = '3??'
print(getWorkflowReplacements(s))

#Salesforce interview question
def getWorkflowReplacements(config):
    MOD = 10**9 + 7
    digits = 10

    dp = [0] * digits

    # initialize first position
    if config[0] == '?':
        for d in range(digits):
            dp[d] = 1
    else:
        dp[int(config[0])] = 1

    for i in range(1, len(config)):
        new_dp = [0] * digits
        total = sum(dp) % MOD

        if config[i] == '?':
            for d in range(digits):
                new_dp[d] = (total - dp[d]) % MOD
        else:
            d = int(config[i])
            new_dp[d] = (total - dp[d]) % MOD

        dp = new_dp

    return sum(dp) % MOD

s = '3??'
print(getWorkflowReplacements(s))