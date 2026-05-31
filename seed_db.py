from werkzeug.security import generate_password_hash
import mysql.connector
from config import Config

def seed():
    try:
        db = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
        cursor = db.cursor()

        # Add Admin User (if not exists)
        admin_pw = generate_password_hash('admin123')
        cursor.execute("INSERT IGNORE INTO users (username, email, password, role) VALUES (%s, %s, %s, %s)",
                      ('admin', 'admin@freshbasket.com', admin_pw, 'admin'))

        # Categories
        cursor.execute("SELECT id, slug FROM categories")
        categories = {slug: id for (id, slug) in cursor.fetchall()}

        # 125 Products with properly curated image URLs
        # (name, description, price, discount_price, category_id, image_url, stock, is_featured)
        products = [
            # --- FRUITS (40 items) ---
            ('Alphonso Mango', 'King of mangoes, sweet and creamy.', 1200.00, 1000.00, categories['fruits'],
             'https://images.unsplash.com/photo-1553279768-865429fa0078?w=500&h=500&fit=crop', 50, 1),

            ('Kashmiri Apple', 'Sweet and crunchy red apples.', 180.00, 160.00, categories['fruits'],
             'https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?w=500&h=500&fit=crop', 100, 1),

            ('Green Apple', 'Tart and crispy green apples.', 220.00, 200.00, categories['fruits'],
             'https://upload.wikimedia.org/wikipedia/commons/f/fe/A_%27Granny_Smith%27_green_apple_from_Australia%2C_photographed_in_India%2C_December_4%2C_2023.jpg', 80, 0),

            ('Robusta Banana', 'Sweet and high-energy bananas.', 60.00, 50.00, categories['fruits'],
             'https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?w=500&h=500&fit=crop', 200, 0),

            ('Red Grapes', 'Sweet seedless red grapes.', 160.00, 140.00, categories['fruits'],
             'https://upload.wikimedia.org/wikipedia/commons/b/b6/Red_grapes_2.jpg', 100, 0),

            ('Black Grapes', 'Juicy seedless black grapes.', 150.00, 130.00, categories['fruits'],
             'https://images.unsplash.com/photo-1423483641154-5411ec9c0ddf?w=500&h=500&fit=crop', 100, 1),

            ('Seedless Grapes', 'Fresh green seedless grapes.', 120.00, 100.00, categories['fruits'],
             'https://images.unsplash.com/photo-1596363505729-4190a9506133?w=500&h=500&fit=crop', 100, 0),

            ('Dragon Fruit (Pink)', 'Exotic pink dragon fruit.', 180.00, 160.00, categories['fruits'],
             'https://upload.wikimedia.org/wikipedia/commons/d/df/Dragon_fruit_%28pitaya%29_on_white_background.jpg', 40, 1),

            ('Dragon Fruit (White)', 'Fresh white dragon fruit.', 170.00, 150.00, categories['fruits'],
             'https://upload.wikimedia.org/wikipedia/commons/4/43/Pitaya_cross_section_ed2.jpg', 40, 0),

            ('Gold Kiwi', 'Sweet and hairless gold kiwis.', 350.00, 300.00, categories['fruits'],
             'https://images.unsplash.com/photo-1618897996318-5a901fa6ca71?w=500&h=500&fit=crop', 50, 1),

            ('Green Kiwi', 'Tangy and vitamin-rich green kiwis.', 100.00, 80.00, categories['fruits'],
             'https://upload.wikimedia.org/wikipedia/commons/c/c3/Kiwi.jpg', 60, 0),

            ('Pomegranate', 'Fresh red pomegranate seeds.', 250.00, 220.00, categories['fruits'],
             'https://images.unsplash.com/photo-1615485290382-441e4d049cb5?w=500&h=500&fit=crop', 50, 0),

            ('Watermelon', 'Big and sweet summer watermelon.', 80.00, 60.00, categories['fruits'],
             'https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=500&h=500&fit=crop', 30, 1),

            ('Muskmelon', 'Refreshing and sweet melon.', 70.00, 60.00, categories['fruits'],
             'https://images.unsplash.com/photo-1571575173700-afb9492e6a50?w=500&h=500&fit=crop', 40, 0),

            ('Papaya (Hybrid)', 'Ripe and sweet hybrid papaya.', 60.00, 50.00, categories['fruits'],
             'https://upload.wikimedia.org/wikipedia/commons/d/d5/2011.09-385-158arp_Mountain_papaya%28Vasconcellea_pubescens%29%2Cfr%28wh%2CTS%29_Naivasha-Gilgil%28Rift_Valley_Prov.%29%2CKE_tue13sep2011-1230h.jpg', 100, 0),

            ('Pineapple', 'Tropical and sweet pineapple.', 100.00, 90.00, categories['fruits'],
             'https://images.unsplash.com/photo-1550258987-190a2d41a8ba?w=500&h=500&fit=crop', 50, 1),

            ('Guava (Pink)', 'Fresh pink guavas from Allahabad.', 120.00, 100.00, categories['fruits'],
             'https://images.unsplash.com/photo-1536657464919-892534f60d6e?w=500&h=500&fit=crop', 40, 0),

            ('Guava (Green)', 'Sweet and crunchy green guavas.', 80.00, 70.00, categories['fruits'],
             'https://images.pexels.com/photos/5946081/pexels-photo-5946081.jpeg?auto=compress&cs=tinysrgb&w=500', 60, 0),

            ('Strawberry (Mahabaleshwar)', 'Fresh and sweet strawberries.', 400.00, 350.00, categories['fruits'],
             'https://images.unsplash.com/photo-1464965911861-746a04b4bca6?w=500&h=500&fit=crop', 30, 0),

            ('Blueberry', 'Antioxidant-rich fresh blueberries.', 500.00, 450.00, categories['fruits'],
             'https://images.unsplash.com/photo-1498557850523-fd3d118b962e?w=500&h=500&fit=crop', 20, 0),

            ('Raspberry', 'Fresh and tart red raspberries.', 600.00, 550.00, categories['fruits'],
             'https://images.unsplash.com/photo-1577003811926-53b288a6e5d0?w=500&h=500&fit=crop', 15, 0),

            ('Blackberry', 'Plump and juicy blackberries.', 550.00, 500.00, categories['fruits'],
             'https://images.unsplash.com/photo-1615484477778-ca3b77940c25?w=500&h=500&fit=crop', 15, 0),

            ('Pear (Babu Gosha)', 'Soft and sweet pears.', 180.00, 160.00, categories['fruits'],
             'https://images.unsplash.com/photo-1514756331096-242fdeb70d4a?w=500&h=500&fit=crop', 40, 0),

            ('Pear (Green)', 'Crunchy green pears.', 150.00, None, categories['fruits'],
             'https://upload.wikimedia.org/wikipedia/commons/9/99/Four_pears.jpg', 40, 0),

            ('Nagpur Orange', 'Juicy and sweet oranges.', 120.00, 100.00, categories['fruits'],
             'https://images.unsplash.com/photo-1547514701-42782101795e?w=500&h=500&fit=crop', 100, 0),

            ('Kinnow Orange', 'Tangy and vitamin-rich kinnows.', 80.00, 70.00, categories['fruits'],
             'https://images.unsplash.com/photo-1611080626919-7cf5a9dbab5b?w=500&h=500&fit=crop', 100, 0),

            ('Custard Apple (Sitaphal)', 'Sweet and creamy sitaphal.', 250.00, 220.00, categories['fruits'],
             'https://images.pexels.com/photos/5946091/pexels-photo-5946091.jpeg?auto=compress&cs=tinysrgb&w=500', 20, 1),

            ('Avocado', 'Buttery and healthy Hass avocados.', 450.00, 400.00, categories['fruits'],
             'https://images.unsplash.com/photo-1523049673857-eb18f1d7b578?w=500&h=500&fit=crop', 30, 1),

            ('Jackfruit', 'Big and sweet yellow jackfruit.', 200.00, None, categories['fruits'],
             'https://images.pexels.com/photos/2543493/pexels-photo-2543493.jpeg?auto=compress&cs=tinysrgb&w=500', 10, 0),

            ('Fresh Figs', 'Sweet and healthy fresh figs.', 350.00, 300.00, categories['fruits'],
             'https://images.unsplash.com/photo-1601379327928-bedfaf9da2d0?w=500&h=500&fit=crop', 20, 0),

            ('Peach', 'Soft and sweet Indian peaches.', 280.00, 250.00, categories['fruits'],
             'https://images.unsplash.com/photo-1603052875302-d376b7c0638a?w=500&h=500&fit=crop', 25, 0),

            ('Plum', 'Juicy and sweet black plums.', 220.00, 200.00, categories['fruits'],
             'https://upload.wikimedia.org/wikipedia/commons/2/24/Red-Plums.jpg', 30, 0),

            ('Nectarine', 'Smooth-skinned sweet nectarines.', 300.00, None, categories['fruits'],
             'https://images.pexels.com/photos/5702781/pexels-photo-5702781.jpeg?auto=compress&cs=tinysrgb&w=500', 15, 0),

            ('Apricot (Fresh)', 'Fresh sweet apricots.', 320.00, 280.00, categories['fruits'],
             'https://images.unsplash.com/photo-1592394533824-9440e5d68530?w=500&h=500&fit=crop', 20, 0),

            ('Cherry (Red)', 'Sweet red cherries.', 700.00, 600.00, categories['fruits'],
             'https://upload.wikimedia.org/wikipedia/commons/5/52/Montmorency_cherries_%283648681426%29.jpg', 10, 0),

            ('Litchi', 'Sweet and fragrant litchis.', 250.00, 200.00, categories['fruits'],
             'https://images.pexels.com/photos/5474640/pexels-photo-5474640.jpeg?auto=compress&cs=tinysrgb&w=500', 40, 1),

            ('Sapodilla (Chikoo)', 'Sweet and grainy chikoo.', 80.00, 70.00, categories['fruits'],
             'https://images.pexels.com/photos/7195133/pexels-photo-7195133.jpeg?auto=compress&cs=tinysrgb&w=500', 100, 0),

            ('Sweet Lime (Mosambi)', 'Fresh and juicy mosambi.', 100.00, 90.00, categories['fruits'],
             'https://images.unsplash.com/photo-1590502593747-42a996133562?w=500&h=500&fit=crop', 100, 0),

            ('Pomelo', 'Large and juicy pomelo fruit.', 150.00, None, categories['fruits'],
             'https://images.pexels.com/photos/5946640/pexels-photo-5946640.jpeg?auto=compress&cs=tinysrgb&w=500', 10, 0),

            ('Wood Apple (Bel)', 'Healthy and sweet wood apple.', 60.00, None, categories['fruits'],
             'https://images.pexels.com/photos/5474628/pexels-photo-5474628.jpeg?auto=compress&cs=tinysrgb&w=500', 30, 0),

            # --- VEGETABLES (40 items) ---
            ('Potato (Alu)', 'Farm fresh red potatoes.', 35.00, 30.00, categories['vegetables'],
             'https://images.unsplash.com/photo-1518977676601-b53f82aba655?w=500&h=500&fit=crop', 500, 1),

            ('Onion (Pink)', 'Fresh pink onions.', 30.00, 25.00, categories['vegetables'],
             'https://images.unsplash.com/photo-1618512496248-a07fe83aa8cb?w=500&h=500&fit=crop', 500, 1),

            ('Red Onion', 'Strong and fresh red onions.', 40.00, 35.00, categories['vegetables'],
             'https://upload.wikimedia.org/wikipedia/commons/9/9f/Red_Onion_on_White.JPG', 300, 0),

            ('White Onion', 'Sweet white onions.', 50.00, 45.00, categories['vegetables'],
             'https://images.unsplash.com/photo-1587735243615-c03f25aaff15?w=500&h=500&fit=crop', 100, 0),

            ('Tomato (Local)', 'Juicy local red tomatoes.', 40.00, 35.00, categories['vegetables'],
             'https://upload.wikimedia.org/wikipedia/commons/2/2a/DFC_5257-_Fresh_tropical_bounty%2C_ripe_cherry_tomatoes%2C_green_limes_and_bananas_piled_together_at_a_local_Thai_market..jpg', 300, 1),

            ('Tomato (Hybrid)', 'Firm and red hybrid tomatoes.', 50.00, 45.00, categories['vegetables'],
             'https://upload.wikimedia.org/wikipedia/commons/c/c3/Organic_home-grown_tomatoes_-_unripe_to_ripe.jpg', 200, 0),

            ('Lady Finger (Bhindi)', 'Tender and fresh okra.', 60.00, 50.00, categories['vegetables'],
             'https://images.pexels.com/photos/7195031/pexels-photo-7195031.jpeg?auto=compress&cs=tinysrgb&w=500', 200, 1),

            ('Cauliflower', 'White and fresh cauliflower.', 60.00, 50.00, categories['vegetables'],
             'https://images.unsplash.com/photo-1568584711075-3d021a7c3ca3?w=500&h=500&fit=crop', 100, 0),

            ('Cabbage', 'Fresh leafy green cabbage.', 40.00, 35.00, categories['vegetables'],
             'https://images.unsplash.com/photo-1594282486552-05b4d80fbb9f?w=500&h=500&fit=crop', 100, 0),

            ('Red Cabbage', 'Nutritious and fresh red cabbage.', 80.00, 70.00, categories['vegetables'],
             'https://upload.wikimedia.org/wikipedia/commons/9/98/Rotkohl_%28Brassica_oleracea_convar%29.JPG', 40, 0),

            ('Broccoli', 'Organic green broccoli crowns.', 150.00, 130.00, categories['vegetables'],
             'https://images.unsplash.com/photo-1459411621453-7b03977f4bfc?w=500&h=500&fit=crop', 50, 1),

            ('Capsicum (Green)', 'Fresh green bell peppers.', 80.00, 70.00, categories['vegetables'],
             'https://images.unsplash.com/photo-1563565375-f3fdfdbefa83?w=500&h=500&fit=crop', 100, 0),

            ('Capsicum (Red)', 'Sweet red bell peppers.', 160.00, 140.00, categories['vegetables'],
             'https://images.unsplash.com/photo-1584270354949-c26b0d5b4a0c?w=500&h=500&fit=crop', 50, 0),

            ('Capsicum (Yellow)', 'Bright yellow bell peppers.', 160.00, 140.00, categories['vegetables'],
             'https://upload.wikimedia.org/wikipedia/commons/9/92/Capsicum_chinense_image_Mobot31753003324867_0189.jpg', 50, 0),

            ('Carrot (Orange)', 'Fresh and crunchy orange carrots.', 70.00, 60.00, categories['vegetables'],
             'https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?w=500&h=500&fit=crop', 150, 0),

            ('Carrot (Red)', 'Sweet and juicy red carrots.', 80.00, 70.00, categories['vegetables'],
             'https://images.unsplash.com/photo-1447175008436-054170c2e979?w=500&h=500&fit=crop', 100, 0),

            ('Bitter Gourd (Karela)', 'Fresh and healthy bitter gourd.', 60.00, 55.00, categories['vegetables'],
             'https://images.pexels.com/photos/5946075/pexels-photo-5946075.jpeg?auto=compress&cs=tinysrgb&w=500', 60, 0),

            ('Bottle Gourd (Lauki)', 'Fresh and tender bottle gourd.', 40.00, 35.00, categories['vegetables'],
             'https://images.pexels.com/photos/6316515/pexels-photo-6316515.jpeg?auto=compress&cs=tinysrgb&w=500', 80, 0),

            ('Ridge Gourd (Turai)', 'Fresh and green ridge gourd.', 50.00, 45.00, categories['vegetables'],
             'https://images.pexels.com/photos/7195059/pexels-photo-7195059.jpeg?auto=compress&cs=tinysrgb&w=500', 60, 0),

            ('Snake Gourd', 'Fresh and long snake gourd.', 40.00, None, categories['vegetables'],
             'https://images.pexels.com/photos/6316514/pexels-photo-6316514.jpeg?auto=compress&cs=tinysrgb&w=500', 40, 0),

            ('Brinjal (Large)', 'Fresh purple bharta brinjal.', 50.00, 40.00, categories['vegetables'],
             'https://upload.wikimedia.org/wikipedia/commons/a/a2/Liat_Portal_for_Foodie_Disorder_-_Eggplant.jpg', 100, 0),

            ('Brinjal (Small)', 'Small and tender purple brinjals.', 60.00, 50.00, categories['vegetables'],
             'https://images.pexels.com/photos/5529599/pexels-photo-5529599.jpeg?auto=compress&cs=tinysrgb&w=500', 100, 0),

            ('Mushroom (Button)', 'Fresh white button mushrooms.', 100.00, 90.00, categories['vegetables'],
             'https://upload.wikimedia.org/wikipedia/commons/d/d8/Button_Mushroom_cultivation.jpg', 60, 0),

            ('Mushroom (Oyster)', 'Fresh exotic oyster mushrooms.', 250.00, 220.00, categories['vegetables'],
             'https://upload.wikimedia.org/wikipedia/commons/9/97/Liat_Portal_for_Foodie_Disorder_-_Pink_tree_oyster_mushrooms.jpg', 20, 0),

            ('Sweet Potato', 'Healthy and sweet orange potatoes.', 70.00, 60.00, categories['vegetables'],
             'https://images.unsplash.com/photo-1591122947157-26bad3a117d2?w=500&h=500&fit=crop', 100, 0),

            ('Beetroot', 'Fresh and red organic beetroots.', 60.00, 50.00, categories['vegetables'],
             'https://upload.wikimedia.org/wikipedia/commons/f/fe/Beets_-_9690511364.jpg', 150, 0),

            ('Radish (White)', 'Fresh and spicy white radish.', 40.00, 30.00, categories['vegetables'],
             'https://upload.wikimedia.org/wikipedia/commons/3/3a/HK_SKD_TKO_%E5%B0%87%E8%BB%8D%E6%BE%B3_Tseung_Kwan_O_%E6%97%A5%E5%87%BA%E5%BA%B7%E5%9F%8E_Lohas_Park_mall_Fresh_Supermarket_food_vegetable_%E7%99%BD%E7%8E%89%E6%98%A5_White_radishes_February_2022_Px3.jpg', 100, 0),

            ('Turnip (Shalgam)', 'Fresh white and purple turnips.', 50.00, 40.00, categories['vegetables'],
             'https://images.pexels.com/photos/6316516/pexels-photo-6316516.jpeg?auto=compress&cs=tinysrgb&w=500', 60, 0),

            ('Spinach (Palak)', 'Fresh green leafy spinach.', 40.00, 30.00, categories['vegetables'],
             'https://images.unsplash.com/photo-1576045057995-568f588f82fb?w=500&h=500&fit=crop', 100, 1),

            ('Fenugreek (Methi)', 'Fresh and healthy methi leaves.', 50.00, 40.00, categories['vegetables'],
             'https://images.pexels.com/photos/6316518/pexels-photo-6316518.jpeg?auto=compress&cs=tinysrgb&w=500', 80, 0),

            ('Coriander (Dhaniya)', 'Fragrant fresh coriander leaves.', 20.00, 15.00, categories['vegetables'],
             'https://images.pexels.com/photos/7412100/pexels-photo-7412100.jpeg?auto=compress&cs=tinysrgb&w=500', 200, 0),

            ('Mint (Pudina)', 'Fresh and refreshing mint leaves.', 30.00, 20.00, categories['vegetables'],
             'https://images.unsplash.com/photo-1628556270448-4d4e4148e1b1?w=500&h=500&fit=crop', 150, 0),

            ('Spring Onion', 'Fresh and crunchy spring onions.', 50.00, 40.00, categories['vegetables'],
             'https://images.pexels.com/photos/6316513/pexels-photo-6316513.jpeg?auto=compress&cs=tinysrgb&w=500', 80, 0),

            ('Cucumber (Local)', 'Cool and refreshing local cucumbers.', 40.00, 35.00, categories['vegetables'],
             'https://upload.wikimedia.org/wikipedia/commons/1/10/Cucumber_%2859441%29.jpg', 200, 0),

            ('Cucumber (English)', 'Seedless and crunchy English cucumbers.', 80.00, 70.00, categories['vegetables'],
             'https://images.unsplash.com/photo-1604977042946-1eecc30f269e?w=500&h=500&fit=crop', 100, 0),

            ('Green Chillies', 'Spicy and fresh green chillies.', 60.00, 50.00, categories['vegetables'],
             'https://images.unsplash.com/photo-1588252303782-cb80119abd6d?w=500&h=500&fit=crop', 200, 0),

            ('Ginger', 'Fresh and spicy ginger roots.', 150.00, 130.00, categories['vegetables'],
             'https://images.unsplash.com/photo-1599940824399-b87987ceb72a?w=500&h=500&fit=crop', 100, 0),

            ('Garlic (Premium)', 'Strong and fresh garlic bulbs.', 200.00, 180.00, categories['vegetables'],
             'https://images.unsplash.com/photo-1540148426945-6cf22a6b2383?w=500&h=500&fit=crop', 100, 0),

            ('Green Peas (Matar)', 'Fresh sweet green peas.', 100.00, 80.00, categories['vegetables'],
             'https://upload.wikimedia.org/wikipedia/commons/5/5c/A_crop_of_peas_-_geograph.org.uk_-_1004517.jpg', 150, 0),

            ('Lemon', 'Fresh and juicy yellow lemons.', 10.00, 8.00, categories['vegetables'],
             'https://images.unsplash.com/photo-1590502593747-42a996133562?w=500&h=500&fit=crop', 500, 0),

            # --- ORGANIC (15 items) ---
            ('Organic Honey', '100% pure raw organic honey.', 500.00, 450.00, categories['organic'],
             'https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=500&h=500&fit=crop', 50, 1),

            ('Organic Jaggery', 'Chemical-free fresh jaggery.', 120.00, 100.00, categories['organic'],
             'https://images.pexels.com/photos/6941010/pexels-photo-6941010.jpeg?auto=compress&cs=tinysrgb&w=500', 100, 0),

            ('Organic Ghee', 'Pure cow milk organic ghee.', 800.00, 750.00, categories['organic'],
             'https://images.pexels.com/photos/6941016/pexels-photo-6941016.jpeg?auto=compress&cs=tinysrgb&w=500', 30, 1),

            ('Organic Turmeric', 'Natural organic turmeric powder.', 200.00, 180.00, categories['organic'],
             'https://images.unsplash.com/photo-1615485290382-441e4d049cb5?w=500&h=500&fit=crop', 100, 0),

            ('Organic Quinoa', 'Healthy organic white quinoa.', 600.00, 550.00, categories['organic'],
             'https://images.unsplash.com/photo-1586201375761-83865001e31c?w=500&h=500&fit=crop', 50, 0),

            ('Organic Oats', 'Steel-cut organic healthy oats.', 400.00, 350.00, categories['organic'],
             'https://images.unsplash.com/photo-1590165482129-1b8b27698780?w=500&h=500&fit=crop', 60, 0),

            ('Organic Almond Oil', 'Cold-pressed organic almond oil.', 1200.00, 1100.00, categories['organic'],
             'https://images.unsplash.com/photo-1617897903246-719242758050?w=500&h=500&fit=crop', 20, 0),

            ('Organic Coconut Oil', 'Pure virgin organic coconut oil.', 500.00, 450.00, categories['organic'],
             'https://images.unsplash.com/photo-1526947425960-945c6e72858f?w=500&h=500&fit=crop', 50, 0),

            ('Organic Flax Seeds', 'High-fiber organic flax seeds.', 200.00, 180.00, categories['organic'],
             'https://images.pexels.com/photos/7195034/pexels-photo-7195034.jpeg?auto=compress&cs=tinysrgb&w=500', 100, 0),

            ('Organic Chia Seeds', 'Nutrient-rich organic chia seeds.', 450.00, 400.00, categories['organic'],
             'https://images.unsplash.com/photo-1514733670139-4d87a1941d55?w=500&h=500&fit=crop', 50, 0),

            ('Organic Green Tea', 'Pure organic green tea leaves.', 350.00, 300.00, categories['organic'],
             'https://images.unsplash.com/photo-1556881286-fc6915169721?w=500&h=500&fit=crop', 80, 0),

            ('Organic Brown Rice', 'Unpolished organic brown rice.', 180.00, 150.00, categories['organic'],
             'https://images.unsplash.com/photo-1586201375761-83865001e31c?w=500&h=500&fit=crop', 200, 0),

            ('Organic Pulses', 'Chemical-free organic mixed pulses.', 250.00, 220.00, categories['organic'],
             'https://images.pexels.com/photos/6316517/pexels-photo-6316517.jpeg?auto=compress&cs=tinysrgb&w=500', 150, 0),

            ('Organic Garlic Powder', 'Pure organic garlic seasoning.', 150.00, None, categories['organic'],
             'https://images.unsplash.com/photo-1540148426945-6cf22a6b2383?w=500&h=500&fit=crop', 50, 0),

            ('Organic Cinnamon', 'Fresh organic cinnamon sticks.', 200.00, 180.00, categories['organic'],
             'https://images.unsplash.com/photo-1587132137056-bfbf0166836e?w=500&h=500&fit=crop', 100, 0),

            # --- DRY FRUITS (15 items) ---
            ('Almonds (Raw)', 'Premium quality raw almonds.', 900.00, 800.00, categories['dry-fruits'],
             'https://images.unsplash.com/photo-1508061253366-f7da158b6d46?w=500&h=500&fit=crop', 100, 1),

            ('Cashews (Whole)', 'Large and crunchy whole cashews.', 1100.00, 1000.00, categories['dry-fruits'],
             'https://upload.wikimedia.org/wikipedia/commons/0/0a/Pile_of_cashews.jpg', 80, 1),

            ('Pistachios (Roasted)', 'Salted and roasted premium pista.', 1300.00, 1200.00, categories['dry-fruits'],
             'https://upload.wikimedia.org/wikipedia/commons/a/a2/Salted_pistachios_photographed_in_West_Bengal%2C_India%2C_by_Yogabrata_Chakraborty%2C_March_7%2C_2023.jpg', 60, 0),

            ('Walnuts (Shelled)', 'High-quality shelled walnuts.', 1000.00, 900.00, categories['dry-fruits'],
             'https://upload.wikimedia.org/wikipedia/commons/6/69/Whole_walnut_kernel_and_shell.jpg', 50, 1),

            ('Raisins (Green)', 'Sweet dried green seedless grapes.', 400.00, 350.00, categories['dry-fruits'],
             'https://images.pexels.com/photos/5473368/pexels-photo-5473368.jpeg?auto=compress&cs=tinysrgb&w=500', 150, 0),

            ('Raisins (Black)', 'Healthy dried black grapes.', 500.00, 450.00, categories['dry-fruits'],
             'https://images.pexels.com/photos/5473369/pexels-photo-5473369.jpeg?auto=compress&cs=tinysrgb&w=500', 100, 0),

            ('Dates (Medjool)', 'Premium large Medjool dates.', 800.00, 750.00, categories['dry-fruits'],
             'https://images.unsplash.com/photo-1604977042946-1eecc30f269e?w=500&h=500&fit=crop', 50, 1),

            ('Dried Apricots', 'Sweet and chewy dried apricots.', 600.00, 550.00, categories['dry-fruits'],
             'https://images.pexels.com/photos/5473370/pexels-photo-5473370.jpeg?auto=compress&cs=tinysrgb&w=500', 40, 0),

            ('Dried Figs (Anjeer)', 'Healthy and sweet dried figs.', 1200.00, 1100.00, categories['dry-fruits'],
             'https://images.unsplash.com/photo-1601379327928-bedfaf9da2d0?w=500&h=500&fit=crop', 30, 0),

            ('Hazelnuts', 'Crunchy and fresh hazelnuts.', 1500.00, 1400.00, categories['dry-fruits'],
             'https://upload.wikimedia.org/wikipedia/commons/3/3f/Hazelnuts.jpg', 20, 0),

            ('Pine Nuts', 'Premium and rare pine nuts.', 3000.00, 2800.00, categories['dry-fruits'],
             'https://images.pexels.com/photos/5473371/pexels-photo-5473371.jpeg?auto=compress&cs=tinysrgb&w=500', 10, 0),

            ('Makhana (Fox Nuts)', 'Crispy and healthy fox nuts.', 600.00, 550.00, categories['dry-fruits'],
             'https://images.pexels.com/photos/6941011/pexels-photo-6941011.jpeg?auto=compress&cs=tinysrgb&w=500', 100, 0),

            ('Prunes', 'Healthy dried plums (prunes).', 500.00, 450.00, categories['dry-fruits'],
             'https://upload.wikimedia.org/wikipedia/commons/9/97/Rosales_-_Dried_Prunus_domestica_d.jpg', 40, 0),

            ('Mixed Dry Fruits', 'A mix of premium nuts and berries.', 1000.00, 900.00, categories['dry-fruits'],
             'https://images.unsplash.com/photo-1606567595334-d39972c85dbe?w=500&h=500&fit=crop', 50, 0),

            ('Pecan Nuts', 'Crunchy and sweet pecans.', 1800.00, 1600.00, categories['dry-fruits'],
             'https://images.pexels.com/photos/5473372/pexels-photo-5473372.jpeg?auto=compress&cs=tinysrgb&w=500', 20, 0),

            # --- JUICES (15 items) ---
            ('Apple Juice', '100% natural apple juice.', 180.00, 160.00, categories['juice'],
             'https://upload.wikimedia.org/wikipedia/commons/e/e5/Measuring_a_green_apple_beside_fresh_juice_in_a_bright_kitchen_setting_during_a_healthy_lifestyle_moment.jpg', 100, 1),

            ('Orange Juice', 'Freshly squeezed Nagpur orange juice.', 150.00, 130.00, categories['juice'],
             'https://images.unsplash.com/photo-1613478223719-2ab802602423?w=500&h=500&fit=crop', 100, 1),

            ('Watermelon Juice', 'Refreshing summer watermelon juice.', 120.00, 100.00, categories['juice'],
             'https://images.unsplash.com/photo-1534353473418-4cfa6c56fd38?w=500&h=500&fit=crop', 150, 1),

            ('Sugarcane Juice', 'Fresh sugarcane juice with ginger.', 80.00, 70.00, categories['juice'],
             'https://images.pexels.com/photos/5946633/pexels-photo-5946633.jpeg?auto=compress&cs=tinysrgb&w=500', 200, 0),

            ('Pomegranate Juice', 'Pure and fresh pomegranate juice.', 250.00, 220.00, categories['juice'],
             'https://images.unsplash.com/photo-1600271886742-f049cd451bba?w=500&h=500&fit=crop', 80, 0),

            ('Mango Juice', 'Thick and sweet Alphonso juice.', 200.00, 180.00, categories['juice'],
             'https://images.unsplash.com/photo-1553279768-865429fa0078?w=500&h=500&fit=crop', 100, 0),

            ('Grape Juice', 'Sweet and fresh purple grape juice.', 160.00, 140.00, categories['juice'],
             'https://images.unsplash.com/photo-1553361371-9b22f78e8b1d?w=500&h=500&fit=crop', 100, 0),

            ('Pineapple Juice', 'Tangy and sweet pineapple juice.', 180.00, 160.00, categories['juice'],
             'https://images.unsplash.com/photo-1550258987-190a2d41a8ba?w=500&h=500&fit=crop', 80, 0),

            ('Mixed Fruit Juice', 'A blend of fresh seasonal fruits.', 150.00, 130.00, categories['juice'],
             'https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?w=500&h=500&fit=crop', 150, 1),

            ('Carrot Juice', 'Healthy and fresh carrot juice.', 120.00, 100.00, categories['juice'],
             'https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?w=500&h=500&fit=crop', 100, 0),

            ('Amla Juice', 'Vitamin-C rich amla juice.', 200.00, 180.00, categories['juice'],
             'https://images.pexels.com/photos/5946639/pexels-photo-5946639.jpeg?auto=compress&cs=tinysrgb&w=500', 50, 0),

            ('Aloe Vera Juice', 'Pure and healthy aloe vera juice.', 250.00, 220.00, categories['juice'],
             'https://images.unsplash.com/photo-1596547609652-9cf5d8d76921?w=500&h=500&fit=crop', 50, 0),

            ('Coconut Water', 'Pure and fresh tender coconut water.', 60.00, 50.00, categories['juice'],
             'https://images.unsplash.com/photo-1525385133512-2f3bdd039054?w=500&h=500&fit=crop', 200, 1),

            ('Lemon Juice', 'Fresh and refreshing lemonade.', 50.00, 40.00, categories['juice'],
             'https://images.unsplash.com/photo-1621263764928-df1444c5e859?w=500&h=500&fit=crop', 200, 0),

            ('Strawberry Shake', 'Creamy and sweet strawberry shake.', 250.00, 220.00, categories['juice'],
             'https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=500&h=500&fit=crop', 60, 0),
        ]

        cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        cursor.execute("TRUNCATE TABLE products")
        cursor.execute("SET FOREIGN_KEY_CHECKS = 1")

        cursor.executemany("""
            INSERT INTO products (name, description, price, discount_price, category_id, image_url, stock, is_featured)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, products)

        db.commit()
        print(f"Database seeded with {len(products)} products! Goal: >100. Actual: {len(products)}")
        cursor.close()
        db.close()

    except Exception as e:
        print(f"Error seeding database: {e}")

if __name__ == '__main__':
    seed()
