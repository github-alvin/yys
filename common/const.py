from .utils import image


# 匹配资源使用分辨率
RESOLUTION = (1152, 679)

# 主界面-探索按钮
GLOBAL_BUTTON_EXPLORE = image("global_explore.png", (0.928, 0.053), RESOLUTION)

# 战斗结束分享按钮
GLOBAL_SIFT_SHARE = image("global_share.png", (0.777, 0.273), RESOLUTION)

# 战斗结束继续界面
GLOBAL_SIFT_CONTINUE = image("global_continue.png", (0.855, 0.395), RESOLUTION)

# 组队队员槽
GLOBAL_TEAMMATES_SLOT = image("team_mates_slot.png", (0.77, 0.046), RESOLUTION)

# 组队开始挑战
GLOBAL_TEAM_CHALLENGE = image("team_challenge.png", (1.05, 0.31), RESOLUTION)