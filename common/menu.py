from navutils import menu
main_menu = menu.Menu('main')
menu.register(main_menu)

# function to check whether a user belongs to a certain group
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 

# function to check wether a user has permissions to view farmers
def can_view_farmers(user, context):
    if user.is_superuser:
        return True
    return user.has_perm('farmer.view_farmerprofile')

# function to check wether a user has permissions to view farmers groups
def can_view_farmer_groups(user, context):
    if user.is_superuser:
        return True
    return user.has_perm('farmer.view_group')

def can_add_farmer_profile(user, context):
    if user.is_superuser:
        return True
    return user.has_perm('farmer.add_farmerprofile')

def can_view_farms(user, context):
    if user.is_superuser:
        return True
    return user.has_perm('farm.view_farm')

def can_view_enterprise(user, context):
    if user.is_superuser:
        return True
    return user.has_perm('farm.view_enterprise')


# menu starts from here
menus = [
    menu.Node(id='dashboard',css_class="sidebar-header", label='<i data-feather="home"></i><span>Dashboard</span>', pattern_name='common:home', link_attrs={'id': 'dashboard'}),
    menu.PassTestNode(
        id='farmer-section',
        css_class="sidebar-header",
        label='<i data-feather="users"></i><span>Farmer</span><i class="fa fa-angle-right pull-right"></i>',
        url='#',
        test=can_view_farmers,
        children=[
            menu.PassTestNode(id='add_farmers',
                              label='<i class="fa fa-circle"></i>Register',
                             
                              pattern_name='farmer:create_farmer', test=can_add_farmer_profile),
            menu.PassTestNode(id='farmers',
                              label='<i class="fa fa-circle"></i>Applications',
                             
                              pattern_name='farmer:farmerprofile_list', test=can_view_farmers),
            menu.PassTestNode(id='farmer_groups',
                              label='<i class="fa fa-circle"></i>Farmer Groups',
                             
                              pattern_name='farmer:farmerprofile_list', test=can_view_farmer_groups),
         
         
        ]
    ),
      menu.PassTestNode(
        id='farm-section',
        css_class="sidebar-header",
        label='<i data-feather="truck"></i><span>Farm</span><i class="fa fa-angle-right pull-right"></i>',
        url='#',
        test=can_view_farms,
        children=[
            menu.PassTestNode(id='farms',
                              label='<i class="fa fa-circle"></i>Farms',
                             
                              pattern_name='farm:farm_list', test=can_view_farms),
            menu.PassTestNode(id='enterprises',
                              label='<i class="fa fa-circle"></i>Enterprises',
                             
                              pattern_name='farm:enterprise_list', test=can_view_enterprise),
 
         
         
        ]
    ),


]
for entry in menus:
    main_menu.register(entry)