def build_profile(firt, last, **user_info):
    profile = {}
    profile['firt_name'] = firt
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
