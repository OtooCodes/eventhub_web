from nicegui import ui

# Load Tailwind + JS into <head>
ui.add_head_html('''
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
<script src="js\script.jsjs"></script>
''')

# NAVBAR
with ui.header().classes('bg-white shadow-md px-6 py-4 flex justify-between items-center relative'):
    ui.label('Event Hub').classes('text-2xl font-bold text-purple-700')

    # Desktop Menu
    with ui.row().classes('hidden md:flex gap-6'):
        ui.link('Home', '#')
        ui.link('Events', '#')
        ui.link('Blog', '#')
        ui.link('Contact', '#')

    # Login button (desktop only)
    ui.button('Login').classes('hidden md:block bg-purple-600 text-white px-4 py-2 rounded-lg')

    # Hamburger Icon (mobile only)
    ui.html('''
    <button id="menu-toggle" class="md:hidden flex flex-col space-y-1">
        <span class="block w-6 h-0.5 bg-purple-700"></span>
        <span class="block w-6 h-0.5 bg-purple-700"></span>
        <span class="block w-6 h-0.5 bg-purple-700"></span>
    </button>
    ''')

# Mobile Dropdown Menu (hidden by default)
ui.html('''
<div id="mobile-menu" class="hidden flex-col space-y-4 bg-white shadow-md p-6 absolute top-16 left-0 right-0 z-50 md:hidden">
    <a href="#" class="text-gray-700 font-medium hover:text-purple-600">Home</a>
    <a href="#" class="text-gray-700 font-medium hover:text-purple-600">Events</a>
    <a href="#" class="text-gray-700 font-medium hover:text-purple-600">Blog</a>
    <a href="#" class="text-gray-700 font-medium hover:text-purple-600">Contact</a>
    <button class="bg-purple-600 text-white px-4 py-2 rounded-lg">Login</button>
</div>
''')

# HERO SECTION
with ui.column().classes('text-center bg-gradient-to-r from-purple-800 to-indigo-800 text-white py-20 px-4'):
    ui.label('MADE FOR THOSE WHO DO').classes('text-3xl md:text-5xl font-extrabold mb-4')
    ui.label('Find and join events around you').classes('text-base md:text-lg mb-6')
    with ui.row().classes('flex flex-col sm:flex-row justify-center gap-3'):
        ui.input('Search events...').classes('px-4 py-2 rounded-lg text-black w-full sm:w-80')
        ui.button('Search').classes('bg-purple-600 px-6 py-2 rounded-lg w-full sm:w-auto')

# UPCOMING EVENTS
ui.label('Upcoming Events').classes('text-2xl md:text-3xl font-bold text-center mt-12 mb-6')
with ui.row().classes('grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 px-6'):
    for i in range(6):
        with ui.card().classes('shadow-lg rounded-xl overflow-hidden transform hover:scale-105 transition'):
            ui.image(f'/static/images/event{i%3+1}.jpg').classes('h-40 w-full object-cover')
            ui.label(f'Exciting Event {i+1}').classes('text-lg font-bold mt-2 px-2')
            ui.label('Join us for an unforgettable experience').classes('text-gray-600 px-2 mb-2')

# CTA - CREATE EVENT
with ui.column().classes('bg-purple-700 text-white text-center py-16 px-6 mt-12 rounded-lg'):
    ui.label('Make your own Event').classes('text-2xl md:text-3xl font-bold')
    ui.button('Create Event').classes('mt-4 bg-white text-purple-700 px-6 py-2 rounded-lg')

# PARTNERS
ui.label('Join these brands').classes('text-2xl md:text-3xl font-bold text-center mt-12 mb-6')
with ui.row().classes('flex flex-wrap justify-center gap-8 px-6'):
    for brand in ['Spotify', 'Google', 'Stripe', 'YouTube', 'Microsoft', 'Zoom', 'Uber', 'Grab']:
        ui.label(brand).classes('text-lg md:text-xl text-gray-700 font-semibold')

# TRENDING
ui.label('Trending Categories').classes('text-2xl md:text-3xl font-bold text-center mt-12 mb-6')
with ui.row().classes('grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 px-6'):
    for category in ['Music Festivals', 'Business Events', 'Technology Meetups']:
        with ui.card().classes('shadow-lg rounded-xl overflow-hidden'):
            ui.image('/static/images/trending.jpg').classes('h-40 w-full object-cover')
            ui.label(category).classes('text-lg font-bold mt-2 px-2')

# BLOG
ui.label('Our Blog').classes('text-2xl md:text-3xl font-bold text-center mt-12 mb-6')
with ui.row().classes('grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 px-6'):
    for i in range(3):
        with ui.card().classes('shadow-lg rounded-xl overflow-hidden'):
            ui.image(f'/static/images/blog{i%2+1}.jpg').classes('h-40 w-full object-cover')
            ui.label(f'Blog Post {i+1}').classes('text-lg font-bold mt-2 px-2')
            ui.label('Tips, news, and insights').classes('text-gray-600 px-2 mb-2')

# FOOTER
with ui.footer().classes('bg-gray-900 text-white text-center py-6 mt-12 px-4'):
    ui.label('© 2025 Event Hub. All Rights Reserved.').classes('text-sm md:text-base')

ui.run()
