import pygame

def pixel_convert(pixel):
    return [pixel[0], pixel[1], pixel[2]]

def cut_all_sprites(file_name: str):
    surfaces = []

    img = pygame.image.load(file_name)
    img_width, img_height = img.get_size()

    start_points = []
    for y in range(0, img_height):
        if pixel_convert(img.get_at([0, y])) == [255,0,0]:
            start_points.append([0, y])
    

    def get_image_sizes(img, start_pos):
        width, height = 0, 0
        while pixel_convert(img.get_at([start_pos[0] + width, start_pos[1]])) != [0, 0, 255]:
            width += 1

        while pixel_convert(img.get_at([start_pos[0], start_pos[1] + height])) != [0, 0, 255]:
            height += 1
        return width, height
        

    for start_point in start_points:
        for x in range(0, img_width):
            if pixel_convert(img.get_at([x, start_point[1]])) == [0,255,0]:
                
                w, h = get_image_sizes(img, [x, start_point[1]])
                surfaces.append(img.subsurface([x + 1, start_point[1] + 1], [w, h]))
    return surfaces

def cut_line_sprites(file_name: str):
    surfaces = []

    img = pygame.image.load(file_name)
    img_width, img_height = img.get_size()

    start_points = []
    for y in range(0, img_height):
        if pixel_convert(img.get_at([0, y])) == [255,0,0]:
            start_points.append([0, y])
    

    def get_image_sizes(img, start_pos):
        width, height = 0, 0
        while pixel_convert(img.get_at([start_pos[0] + width, start_pos[1]])) != [0, 0, 255]:
            width += 1

        while pixel_convert(img.get_at([start_pos[0], start_pos[1] + height])) != [0, 0, 255]:
            height += 1
        return width, height
        

    for start_point in start_points:
        line = []
        for x in range(0, img_width):
            if pixel_convert(img.get_at([x, start_point[1]])) == [0,255,0]:
                
                w, h = get_image_sizes(img, [x, start_point[1]])
                line.append(img.subsurface([x + 1, start_point[1] + 1], [w, h]))
        surfaces.append(line)
    return surfaces

def convert_surfaces_to_sprites(surfaces, scale):
    sprites = []
    for surf in surfaces:
        sp = Sprite.load_surf(surf)
        sp.scale = scale
        sprites.append(sp)
    return sprites

class Sprite:
    @classmethod
    def load_sprite(self, filename: str):
        img = pygame.image.load(filename)
        sp = Sprite(img)
        return sp
    
    @classmethod
    def load_surf(self, surf: pygame.Surface):
        sp = Sprite(surf)
        return sp

    def __init__(self, image: pygame.Surface) -> 'Sprite':
        self.start_image = image
        self.scale = 1
        self.angle = 0
        self.pos = [0, 0]
    
    def rotate(self, angle):
        self.angle += angle

    def render(self, surf: pygame.Surface):
        
        scaled_image = pygame.transform.scale(self.start_image, (int(self.start_image.get_width() * self.scale), int(self.start_image.get_height() * self.scale)))
        rotated_image = pygame.transform.rotate(scaled_image, self.angle).convert()
        rotated_image.set_colorkey((0,0,0))
        
        surf.blit(rotated_image, [self.pos[0]-rotated_image.get_width()/2, self.pos[1]-rotated_image.get_height()/2])

class SpriteAnimate:
    def __init__(self, sprites: list, tick_to_update = 10) -> None:
        self.sprites = sprites
        self.sprite_index = 0
        self.started = False
        self.tick_to_update = tick_to_update
        self.timer = 0

    def start(self):
        self.started = True
        return self
    
    def stop(self):
        self.started = False
        return self
    
    def rotate(self, angle):
        for sprite in self.sprites:
            sprite.rotate(angle)

    @property
    def angle(self):
        return self.sprites[0].angle
    
    @angle.setter
    def angle(self, angle):
        for sprite in self.sprites:
            sprite.angle = angle

    @property
    def scale(self):
        return self.sprites[0].scale
    
    @scale.setter
    def scale(self, scale):
        for sprite in self.sprites:
            sprite.scale = scale

    @property
    def pos(self):
        return self.sprites[0].pos
    
    @pos.setter
    def pos(self, pos):
        for sprite in self.sprites:
            sprite.pos = pos
    
    def render(self, surface: pygame.Surface):
        self.sprites[self.sprite_index].render(surface)

    def update(self):
        if self.started:
            self.timer+=1
        if self.timer>=self.tick_to_update:
            self.sprite_index+=1
            self.timer = 0
        if self.sprite_index==len(self.sprites):
            self.sprite_index = 0


    