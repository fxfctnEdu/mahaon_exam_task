from django.shortcuts import render

# Create your views here.

posts = [
    {
        "id": 0,
        "author": "Lacy Abbott",
        "text": "Labore commodo qui aute quis veniam magna enim veniam incididunt. Elit culpa ullamco sint sit nisi nostrud. Anim minim excepteur veniam occaecat. Id laborum reprehenderit commodo ex aute id consectetur esse ex in.\r\nDolor esse et incididunt anim id sint eu fugiat anim dolor fugiat. Incididunt nostrud tempor anim irure dolor ea ad consequat sit aliquip sint ipsum ut voluptate. Do quis nisi nostrud laboris anim et laborum veniam eiusmod. Laboris cillum velit voluptate ullamco. Laboris ut ex anim deserunt voluptate duis pariatur non duis qui velit.\r\nMinim consectetur consectetur nisi minim velit consectetur et amet deserunt do quis aliqua. Tempor do non sint et quis cupidatat aute veniam enim quis dolore do tempor. Quis eu amet cupidatat nulla ipsum amet labore ullamco do occaecat exercitation laboris. Consequat sint consequat elit velit enim fugiat dolor ad qui. Magna excepteur et qui labore cillum cillum tempor aliqua Lorem ipsum consequat. Non excepteur ex voluptate quis eiusmod consectetur laboris fugiat aliqua ad. Veniam deserunt nulla sint eiusmod tempor elit pariatur est ea quis commodo ipsum aliquip excepteur.\r\n",
        "title": "Elit aliquip nulla commodo laborum in nulla pariatur adipisicing et aliqua",
        "date": "Wed Mar 28 1979 07:42:05 GMT+0600 (+06)"
    },
    {
        "id": 1,
        "author": "Kitty Tanner",
        "text": "Enim minim nostrud consequat consequat laboris veniam nulla consequat exercitation tempor amet exercitation. Pariatur ipsum irure duis veniam consectetur cupidatat. Ipsum ex officia esse officia adipisicing eiusmod qui.\r\nCillum aliquip esse ex voluptate velit enim tempor reprehenderit duis. Voluptate est voluptate culpa mollit adipisicing elit consequat sunt. Ut occaecat aute cupidatat anim cillum reprehenderit do adipisicing adipisicing aliquip consectetur ex duis. Velit velit do sint ut mollit laborum ipsum officia. Ipsum nostrud culpa eiusmod id. Ad aute eiusmod ut dolor. Amet aliquip excepteur occaecat voluptate amet culpa pariatur et cillum voluptate ut fugiat.\r\nNulla ex anim velit ad ex mollit nulla est elit voluptate mollit occaecat. In esse ad ad aute culpa cillum deserunt anim in. Cillum cillum labore sit ad fugiat nostrud aliquip et. Proident consectetur Lorem elit do do proident nisi consequat mollit consectetur qui minim pariatur aute. Nostrud deserunt incididunt cupidatat adipisicing proident voluptate ea exercitation officia exercitation ex fugiat magna dolor.\r\n",
        "title": "Ea elit id id consequat",
        "date": "Tue Sep 24 2002 15:56:49 GMT+0700 (+07)"
    },
    {
        "id": 2,
        "author": "Weaver Byrd",
        "text": "Aute adipisicing fugiat irure aliqua nulla. Excepteur sint velit aliquip pariatur occaecat do sint occaecat minim ipsum mollit quis Lorem. Amet aliquip occaecat cillum cillum anim proident elit ad sint commodo ullamco deserunt sunt sunt. Labore ea anim magna do sint. Qui sunt ipsum reprehenderit occaecat deserunt Lorem consequat dolor.\r\nNostrud duis elit anim id amet laborum ullamco non esse commodo ex ut incididunt aliquip. Qui mollit dolore dolor dolor. Veniam aliqua esse sit culpa sunt exercitation.\r\nVelit cillum officia est est proident eiusmod amet eiusmod reprehenderit ipsum. Aliquip cillum incididunt ea tempor ea voluptate ad qui id dolor. Quis dolor Lorem esse do id occaecat eu est dolor labore non proident.\r\n",
        "title": "Reprehenderit et laborum culpa proident ad ad incididunt irure consequat esse",
        "date": "Mon Apr 14 1986 15:04:53 GMT+0700 (+07)"
    },
    {
        "id": 3,
        "author": "Foley Barlow",
        "text": "Elit in commodo proident cupidatat fugiat nisi et tempor et aliqua mollit minim. Laborum consectetur labore culpa veniam sunt culpa minim anim officia commodo incididunt ut ipsum ex. Aliquip quis nulla consectetur reprehenderit voluptate quis consequat mollit id consequat. Culpa adipisicing ipsum pariatur id do incididunt tempor exercitation proident esse magna cillum fugiat pariatur. Mollit ut magna laboris proident do exercitation qui esse laborum. Ex ut anim incididunt elit aliquip labore duis incididunt nisi magna dolor ut.\r\n",
        "title": "Ea consectetur enim ipsum dolor do irure ipsum duis fugiat id cillum",
        "date": "Thu Feb 28 1991 02:58:40 GMT+0600 (+06)"
    },
    {
        "id": 4,
        "author": "Alana Benton",
        "text": "Reprehenderit cillum laborum ad tempor labore dolor sunt. Dolore occaecat ad Lorem consectetur adipisicing officia non magna. Sunt ex sunt magna nulla voluptate cillum voluptate. Ea esse ullamco cupidatat adipisicing ex minim. Ut incididunt elit reprehenderit proident dolor. Mollit culpa proident esse reprehenderit tempor ea ullamco amet et. Nostrud velit occaecat excepteur dolor ipsum mollit id non reprehenderit.\r\n",
        "title": "Labore magna sunt esse amet do non adipisicing",
        "date": "Fri Feb 06 1976 14:46:20 GMT+0600 (+06)"
    }
]


def get_index(request):
    return render(request, 'blog/index.html', {'posts': posts})


def get_post(request):
    pass
