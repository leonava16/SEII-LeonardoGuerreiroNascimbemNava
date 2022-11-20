FloatLayout:
  id: tela
  BoxLayout: 
    canvas:
      Color:
        rgba: 0.92, 0.92, 0.92, 1
      Rectangle:
        size: self.size
        pos: self.pos
    orientation: 'vertical'
    AppBar:
    Space:
    Menu:
    ScrollView:
      BoxLayout:
        size_hint_y: None
        height: self.minimum_height
        orientation: 'vertical'
        Chat:
        Chat:
        Chat:
        Chat:
        Chat:
        Chat:
        Chat:
        Widget:
  Lista:

<Space@Widget>:
  canvas:
    Color:
      rgba:0,0.3,0.13,1
    Rectangle:
      size: self.size
      pos: self.pos
  size_hint_y: None
  height: '16dp'

<AppBar@BoxLayout>:
  padding: '6dp'
  canvas:
    Color:
      rgba:0,0.3,0.13,1
    Rectangle:
      size: self.size
      pos: self.pos
  size_hint_y: None
  height: '50dp'

  Label:
    text: 'Whatsapp 2 - NFT Edition'
    bold: True
    font_size: '22dp'
    haling: 'left'
    text_size: self.size
    valign: 'center'
    padding_x: '10dp'
  Icon:
    background_normal: 'lupa.png'
  Icon:
    background_normal: 'more.png'
  
<Menu@BoxLayout>:
  canvas:
    Color:
      rgba:0,0.3,0.13,1
    Rectangle:
      size: self.size
      pos: self.pos
  padding: '2dp'
  spacing: '10dp'
  size_hint_y: None
  height: '35dp'
  Icon: 
    background_normal: 'camera.png'
  MenuButton:
    text: 'CHATS'
    active: True
  MenuButton:
    text: 'STATUS'
    active: False
  MenuButton:
    text: 'CALLS'
    active: False

<Foto@Widget>:
  canvas:
    Color:
      rgba: 1, 1, 1, 1
    Ellipse:
      size: self.size
      pos: self.pos
      source: 'logozap.png'
  size_hint_x: None
  width: self.height

<ListaItem@Label>:
  color: 0, 0, 0, 0.7
  size_hint_y: None
  height: '50dp'

<Lista@AnchorLayout>:
  anchor_x: 'right'
  anchor_y: 'top'
  padding: '50dp'
  BoxLayout:
    canvas: 
      Color:
        rgba: 0.92, 0.92, 0.92, 1
      Rectangle:
        size: self.size
        pos: self.pos
    size_hint: None, None
    height: self.minimum_height
    width: '200dp'
    orientation: 'vertical'
    ListaItem:
      text: 'Opção 1'
    ListaItem:
      text: 'Opção 2'
    ListaItem:
      text: 'Opção 3'

<Chat@BoxLayout>:
  canvas: 
    Color:
      rgba: 0, 0, 0, 0.2
    Line:
      width: 1
      points: self.x + self.height, self.y, self.x + self.width - 20, self.y
  size_hint_y: None
  height: '100dp'
  padding: '13dp'
  Foto:
  BoxLayout:
    orientation: 'vertical'
    padding: '13dp'
    Label:
      text: 'Nome do grupo ou chat'
      color: 0, 0, 0, 1
      text_size: self.size
      halign: 'left'
      valign: 'center'
      bold: True
    Label:
      text: 'Charlin: ultima mensagem do chat'
      color: 0, 0, 0, 0.8
      text_size: self.size
      halign: 'left'
      valign: 'center'
  BoxLayout:
    size_hint_x: None
    width: '100dp'
    padding: '7dp'
    Label:
      text: '21:01PM'
      color: 0, 0, 0, 0.5
      text_size: self.size
      valign: 'top'
      halign: 'right'

<MenuButton@Button>:
  active: False
  canvas: 
    Color:
      rgba: 1, 1, 1, 1
    Line: 
      width: 4 if root.active else 0.1
      points: self.x, self.y, self.x + self.width, self.y
  background_color: 0, 0, 0, 0
  bold: True
  color: (1, 1, 1, 1) if root.active else (1, 1, 1, 0.5)


<Icon@Button>:
  active: False
  size_hint_x: None
  width: self.height
  border: 0, 0,0,0