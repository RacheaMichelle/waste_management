from django.core.management.base import BaseCommand
from education.models import Resource


class Command(BaseCommand):
    help = 'Create or update educational resources for various waste types.'

    def handle(self, *args, **kwargs):
        resources = [
            {
                "title": "♻️ Plastic Recycling in Uganda",
                "waste_type": "plastic",
                "category": "recycling",
                "image": "resources/plastic_recycling_uganda.jpg",
                "recycling_process": """🌟 UGANDA PLASTIC RECYCLING PROCESS:

1. 📍 COLLECTION: Community members gather plastic waste from homes, markets, and public spaces
2. 🎯 SORTING: Separate by type - PET bottles, HDPE containers, plastic bags
3. 🧼 CLEANING: Wash thoroughly at community washing stations
4. ✂️ SHREDDING: Local machines cut plastic into small flakes
5. 🔥 MELTING: Heat to create new raw material
6. 🎨 MANUFACTURING: Create beautiful Ugandan products!

💡 Local Success: Women's groups in Kampala are turning plastic waste into colorful baskets and household items!""",
                "products_made": "🏺 New bottles, 🪑 furniture, 🧱 construction materials, 🎨 Ugandan crafts, 👗 clothing fabric",
                "making_process": """🎨 HOW TO MAKE UGANDAN PLASTIC PRODUCTS:

FLEECE JACKETS FROM BOTTLES:
1. Collect PET plastic bottles from your community
2. Remove caps and labels, wash thoroughly
3. Local machines shred into plastic flakes
4. Melt and extrude into polyester fibers
5. Spin into yarn and weave into fabric
6. Ugandan tailors create beautiful jackets!

PLASTIC LUMBER FOR CONSTRUCTION:
1. Collect mixed plastic waste
2. Shred into small pieces
3. Mix with natural colorants
4. Heat and compress in molds
5. Create durable planks for furniture

🌟 Ugandan Innovation: Youth groups are creating plastic lumber for school desks!""",
                "tutorial_links": "https://youtu.be/Hf2Te2OsYqg?si=3l_hcEt9U3QzXTjp,https://youtu.be/cNPEH0GOhRw?si=xxBFKPFKfdR9g60H",
                "uganda_spotlight": "🌍 UGANDA SPOTLIGHT: The Women's Plastic Recycling Collective in Kampala has created 50+ jobs and recycled over 10 tons of plastic!",
                "fun_fact": "💡 FUN FACT: It takes about 10 plastic bottles to make enough fabric for a traditional Ugandan shirt!"
            },
            {
                "title": "📚 Paper Recycling - Ugandan Style",
                "waste_type": "paper",
                "category": "recycling",
                "image": "resources/paper_recycling_uganda.jpg",
                "recycling_process": """📖 PAPER RECYCLING UGANDAN WAY:

1. 📦 COLLECTION: Gather paper from schools, offices, and markets
2. 🎨 SORTING: Separate by type - cardboard, office paper, newspapers
3. 💧 PULPING: Mix with water in large drums
4. 🧽 SCREENING: Remove staples and contaminants
5. 🎭 FORMING: Spread pulp onto screens in the sun
6. ☀️ DRYING: Uganda's sunshine naturally dries the paper

🌱 Local Touch: Many schools use paper recycling as science projects!""",
                "products_made": "📒 Notebooks for schools, 🎁 Gift cards, 🏠 Insulation, 🥚 Egg cartons, 📦 Packaging",
                "making_process": """🎯 MAKE RECYCLED PAPER AT HOME:

UGANDAN HANDMADE PAPER:
1. Tear used paper into small pieces
2. Soak in water overnight
3. Blend into smooth pulp (add natural dyes!)
4. Pour onto a screen in a wooden frame
5. Press with cloth to remove water
6. Dry in the Ugandan sun
7. Create beautiful handmade paper

💼 Business Opportunity: Many artisans sell handmade paper for wedding invitations and certificates!""",
                "tutorial_links": "https://youtu.be/5xrWrKIVBgo?si=dtxVfUdM6-0kwcuc",
                "uganda_spotlight": "🏫 UGANDA SPOTLIGHT: St. Mary's College in Kisubi runs a student-led paper recycling program that funds school activities!",
                "fun_fact": "🌳 FUN FACT: Recycling one ton of paper saves 17 mature trees - that's like saving a small Ugandan forest!"
            },
            {
                "title": "🍶 Glass Recycling - Traditional & Modern",
                "waste_type": "glass",
                "category": "recycling", 
                "image": "resources/glass_recycling_uganda.jpg",
                "recycling_process": """🔮 GLASS RECYCLING IN UGANDA:

1. 🍾 COLLECTION: Gather bottles from bars, hotels, and homes
2. 🎨 SORTING: Separate by color - clear, green, brown
3. 🧹 CLEANING: Remove labels and contaminants
4. 💥 CRUSHING: Break into 'cullet' (small pieces)
5. 🔥 MELTING: Traditional kilns or modern furnaces
6. 🎨 CRAFTING: Create new products

🔄 Traditional Method: Many local breweries still reuse bottles the old-fashioned way - washing and refilling!""",
                "products_made": "🫙 New bottles, 🏺 Decorative items, 🎨 Art pieces, 🪞 Glass beads, 🏗️ Construction aggregate",
                "making_process": """🌟 CREATE GLASS PRODUCTS:

TRADITIONAL GLASS BEADS:
1. Collect broken glass by color
2. Crush into fine powder
3. Mix with natural binders
4. Shape into beads using molds
5. Fire in traditional kilns
6. Create beautiful jewelry

MODERN RECYCLING:
1. Mix crushed glass with raw materials
2. Melt in improved furnaces
3. Create new bottles and containers

👩‍🎨 Artisan Success: Women in Jinja create beautiful glass bead jewelry sold to tourists!""",
                "tutorial_links": "https://youtu.be/b4Af2RATDLs?si=k62ChjZanKXrLI2y,https://youtu.be/Ow5LeG-zzyg?si=fgyx6_ki51kZJgmk",
                "uganda_spotlight": "💎 UGANDA SPOTLIGHT: The Jinja Glass Artists Cooperative turns waste glass into beautiful art that supports 20+ families!",
                "fun_fact": "∞ FUN FACT: Glass can be recycled infinitely without losing quality - it's the ultimate recycling champion!"
            },
            {
                "title": "🌿 Composting - Uganda's Natural Solution",
                "waste_type": "organic",
                "category": "composting",
                "image": "resources/composting_uganda.jpg",
                "recycling_process": """🌱 UGANDAN COMPOSTING METHODS:

1. 🍌 COLLECTION: Kitchen scraps, garden waste, market leftovers
2. 📊 SORTING: Separate from plastics and other contaminants
3. 🎪 PILE METHOD: Traditional heap composting
4. 🐛 VERMICOMPOSTING: Using local earthworms
5. 📦 BIN COMPOSTING: Modern container methods
6. 🌿 MATURING: Uganda's climate speeds up the process!

🌧️ Seasonal Tip: Rainy season is perfect for composting - nature provides the water!""",
                "products_made": "🌿 Rich compost for gardens, 💪 Soil conditioner, 🍃 Mulch, 🌱 Organic fertilizer, 🔋 Biogas potential",
                "making_process": """🏡 COMPOST UGANDAN STYLE:

TRADITIONAL HEAP COMPOSTING:
1. Choose a shaded spot in your compound
2. Layer green materials (food scraps) and brown materials (dry leaves)
3. Turn every 2 weeks with a jembe
4. Keep moist like a well-wrung sponge
5. Ready in 2-3 months!

MODERN VERMICOMPOSTING:
1. Get local composting worms
2. Set up simple wooden boxes
3. Feed kitchen scraps regularly
4. Harvest rich worm castings

💰 Economic Benefit: Good compost can increase crop yields by 30%!""",
                "tutorial_links": "https://youtu.be/zy70DAaeFBI?si=oqqkvUk5gxFgJMmu",
                "uganda_spotlight": "🌾 UGANDA SPOTLIGHT: The Kawempe Urban Farmers group produces 5 tons of compost monthly from market waste!",
                "fun_fact": "🍌 FUN FACT: Banana peels are composting superstars - they break down quickly and add valuable potassium to soil!"
            },
            {
                "title": "🔩 Metal Recycling - Uganda's Informal Economy",
                "waste_type": "metal",
                "category": "recycling",
                "image": "resources/metal_recycling_uganda.jpg",
                "recycling_process": """⚡ METAL RECYCLING IN UGANDA:

1. 🔍 COLLECTION: Informal collectors gather scrap metal
2. 🧲 SORTING: Separate ferrous (magnetic) and non-ferrous metals
3. 💰 TRADING: Local scrap yards buy and sort materials
4. 🔥 PROCESSING: Small-scale smelting and forging
5. 🎨 MANUFACTURING: Create new products

🛠️ Local System: Uganda has a well-established informal metal recycling network that supports many families!""",
                "products_made": "🪚 Tools, 🪑 Furniture, 🏠 Construction materials, 🔩 Hardware, 🎨 Art sculptures",
                "making_process": """🛠️ CREATE FROM SCRAP METAL:

TRADITIONAL BLACKSMITHING:
1. Collect scrap iron and steel
2. Heat in charcoal forges
3. Hammer into tools and hardware
4. Quench for hardening
5. Create useful household items

MODERN RECYCLING:
1. Sort aluminum cans separately
2. Melt in improved furnaces
3. Cast into new products
4. Create aluminum windows and frames

👨‍🏭 Skills Preservation: Many young Ugandans are learning traditional blacksmithing skills!""",
                "tutorial_links": "https://youtu.be/UIPA-ZagWww?si=9mbZ72Adeyu9R84Q",
                "uganda_spotlight": "🔧 UGANDA SPOTLIGHT: The Kisenyi Metal Workers Association recycles over 2 tons of metal monthly and trains youth in metalwork!",
                "fun_fact": "💡 FUN FACT: Recycling aluminum saves 95% of the energy needed to make new aluminum - that's like powering a TV for 3 hours with one can!"
            }
        ]

        # First, let's clear existing resources to avoid unique constraint issues
        Resource.objects.all().delete()
        self.stdout.write("🧹 Cleared existing resources...")

        created_count = 0

        for data in resources:
            try:
                # Create new resource
                resource = Resource.objects.create(
                    title=data["title"],
                    waste_type=data["waste_type"],
                    category=data["category"],
                    image=data.get("image", ""),
                    recycling_process=data["recycling_process"],
                    products_made=data["products_made"],
                    making_process=data["making_process"],
                    tutorial_links=data.get("tutorial_links", ""),
                    uganda_spotlight=data.get("uganda_spotlight", ""),
                    fun_fact=data.get("fun_fact", "")
                )
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"✅ Created resource for: {data['waste_type']}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"❌ Error creating resource for {data['waste_type']}: {e}"))

        self.stdout.write(self.style.SUCCESS(f"\n🎉 Successfully created {created_count} resources!"))
        self.stdout.write("📸 Remember to add Uganda-themed photos to the resources/ directory!")