# YUML Helper

Syntax Cheat Sheet
------

Class
------
    [Customer]->[Order]               // Association
    [Customer]<>->[Order]             // Aggregation
    [Customer]++->[Order]             // Composition
    [Customer]1-0..1>[Order]          // Cardinality
    [Customer]1-0..orders 1>[Order]   // Assoc Labels
    [Customer]-.-[note: DAO]          // Notes
    [Customer]^[Member]               // Inheritance
    [Customer|name;address|save()]    // Properties
    [≪IDisposable≫;Customer]          // Interface
    [Customer|var arr［］ ]            // Brackets
    [Customer {bg:green}]             // Colour

Use Case
------
    [Customer]                        // Actor
    [Customer]-(Place Order)          // Actor to Use Case
    (Order)>(Cancel)                  // Extend
    (Order)<(Pay)                     // Include
    [Member]^[Customer]               // Actor Inheritance

Activity
------
    (start)-|a|
    |a|->(Grind Coffee)->(Pour Shot)->(Froth Milk)->(Pour Coffee)->|b|
    |a|->(Fry Eggs)->(Make Toast)->(Butter Toast)->|b|
    |b|-><c>[want another coffee]->(Grind Coffee)
    <c>[ready to go]->(end)

Color Codes
------

[Color Code](https://yuml.me/69f3a9ba.svg)

| a-z|names|
| :---: | :---: |
|_a_| All the colours of yUML | aliceblue | antiquewhite | aquamarine | azure |
|_b_| beige | bisque | black | blue | blueviolet | brown | burlywood |
|_c_| cadetblue | chartreuse | chocolate | coral | cornsilk | crimson | cyan |
|_d1_| darkgoldenrod | darkorange | darkorchid | darksalmon | darkseagreen | darkslateblue | darkviolet | 
|d2| deeppink | deepskyblue | dodgerblue |
|f| firebrick | floralwhite | forestgreen |
|g| gainsboro | ghostwhite | gold | goldenrod | gray | green | greenyellow |
|h| honeydew | hotpink |
|_i_| indianred |
|k| khaki |
|l1| lavender | lavenderblush | lawngreen | lemonchiffon | lightblue | lightcoral | 
|l2| lightcyan | lightgray | lightpink | lightsalmon | lightseagreen | lightskyblue | 
|l3| lightslategray | lightsteelblue | lightyellow | limegreen | linen |
|m1| magenta | maroon | mediumaquamarine | mediumblue | mediumorchid | mediumpurple | 
|m2| mediumseagreen | mediumslateblue | mediumspringgreen | 
|m3| mediumturquoise | mediumvioletred | mistyrose | moccasin |
|n| navajowhite |
|o| oldlace | olivedrab | orange | orangered | orchid | 
|p1| palegoldenrod | palegreen | paleturquoise | palevioletred | 
|p2| papayawhip | peachpuff | peru | pink | plum | powderblue | purple | 
|r| red | rosybrown | royalblue |
|s1| saddlebrown | salmon | sandybrown | seagreen | seashell | 
|s2| sienna | skyblue | slateblue | slategray | snow | springgreen | steelblue |
|t| tan | thistle | tomato | turquoise |
|v| violet 
|w| wheat | white | whitesmoke |
|y| yellow | yellowgreen |


YUML Examples with images
-----

[Class diagram in Scruffy images](https://yuml.me/diagram/scruffy/class/samples)
[Activity diagram in Scruffy images](https://yuml.me/diagram/scruffy/activity/samples)
[Usecase diagram in Scruffy images](https://yuml.me/diagram/scruffy/usecase/samples)

[Class diagram in Plain images](https://yuml.me/diagram/plain/class/samples)
[Activity diagram in Plain images](https://yuml.me/diagram/plain/activity/samples)
[Usecase diagram in Plain images](https://yuml.me/diagram/plain/usecase/samples)

