from flet import *
#36:39
def main(page: Page):
    BG = '#041955'
    FWG = '#97b4ff'
    FG = '#3450a1'
    PINK = '#eb06ff'

    create_task_view = Container(

    )


    tasks = Column(
        controls=[]
    )

    categoriesCard = Row(
        scroll='auto'
    )

    categories = ['Business', 'Family', 'Friends']
    for i, category in enumerate(categories):
        categoriesCard.controls.append(
            Container(
            bgcolor=BG, 
            height=110,
            width=170,
            padding= 15,
            border_radius=20,
            content=Column(
            controls=[
            Text('40 tasks',color='white'),
            Text(category,color='white'),
            Container(
            width=160,
            height=5,
            bgcolor='white12',
            border_radius=20,
            padding=padding.only(right=i*20),
            content=Container(
            bgcolor=PINK
            ),
            )
            ],
            ),
            )
        )

    first_page_contents = Container(
        content=Column(
        controls=[
        Row(
         controls=[
             Icon(icons.MENU,color='white'),
                    
            Container(width=250),
       
             Icon(icons.SEARCH,color='white'),
                    
        
             Icon(icons.NOTIFICATIONS_OUTLINED,color='white')
                    
                ]
            ),
           Text(value='What\'s up, Wed!', color='white') ,
           Text(value='CATEGORIES',color='white'),
           Container(
        padding=padding.only(top=10, bottom=20),
        content= categoriesCard

           ),
           Container(height=20),
           Text('TODAY\'S TASKS',color='white'),
           Stack(
        controls=[
        tasks,
        FloatingActionButton( icon= icons.ADD,on_click=lambda _: page.go ('/create_task'))
        ]
           )
         ],
         )
    )

    page_1 = Container()
    page_2 = Row(
        controls=[
        Container(
        width=400,
        height=850,
        bgcolor=FG,
        border_radius=35,
        padding= padding.only(
          top=50, left=20,
          right=20, bottom=5
        ),
        content=Column(
        controls=[
            first_page_contents
        ]
        )
     )
        ]
    )
    container = Container(
        width=400, height=850, bgcolor=BG, border_radius=35, content=Stack(
        controls=[
        page_1,
        page_2
        ]
        )
    )

    pages = {
        '/':View(
            "/",
            [
                container
            ],
        ),
        '/create_task': View(
                "/create_task",
                [
                    create_task_view
                ],
        )
    }

    def route_change(route):
        page.views.clear()
        page.views.append(
          pages[page.route]
        )
    page.add(container) 

    page.on_route_change = route_change
    page.go(page.route)

app(target=main, view= WEB_BROWSER)
