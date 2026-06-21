from flask import Flask, render_template, request, jsonify
import random
import time

app = Flask(__name__)

# ══════════════════════════════════════════════════════════
#  KNOWLEDGE BASE — Saad Engraving Tumbler Shop
# ══════════════════════════════════════════════════════════
KB = [
    # ── BRANDS ──────────────────────────────────────────
    {
        "keys": ["what brands", "which brands", "sell", "brands available", "tumbler brands", "offer", "kya bechte", "products"],
        "a": "Hum do premium brands sell karte hain:\n\n🥤 Owala — FreeSip bottles 24oz & 40oz. Built-in straw ke saath on-the-go hydration ke liye best hai.\n\n☕ Stanley — Quencher & Adventure tumblers 20oz, 30oz & 40oz. All-day use ke liye perfect.\n\nDono brands 100% authentic hain aur optional laser engraving ke saath available hain! ✨"
    },
    {
        "keys": ["owala", "free sip", "freesip"],
        "a": "Owala FreeSip tumblers hamare bestseller hain! 🔥\n\n• Sizes: 24oz aur 40oz\n• Double-wall vacuum insulated stainless steel\n• 2-in-1 FreeSip lid — directly pee sakte hain ya built-in straw use kar sakte hain\n• Multiple colors available\n• 24 ghante tak cold rakhta hai\n• Cup holders mein fit hota hai\n\nPlain ya custom laser engraving ke saath available hai!"
    },
    {
        "keys": ["stanley", "quencher"],
        "a": "Stanley tumblers iconic hain! ☕\n\n• Sizes: 20oz, 30oz, aur 40oz Quencher\n• Recycled stainless steel, vacuum insulated\n• 2 din cold / 7 ghante hot rakhta hai\n• Iconic handle + comfortable grip\n• Leakproof lid with straw included\n\nGifting ke liye perfect — specially personal engraving ke saath! 🎁"
    },

    # ── PRICING ─────────────────────────────────────────
    {
        "keys": ["price", "cost", "how much", "rate", "pricing", "charges", "kitna", "daam", "qeemat", "kitne ka"],
        "a": "Hamare current prices:\n\n🥤 Owala (plain):\n  • 24oz — Rs. 3,500\n  • 40oz — Rs. 4,200\n\n☕ Stanley (plain):\n  • 20oz — Rs. 4,500\n  • 30oz — Rs. 5,500\n  • 40oz — Rs. 6,500\n\n✏️ Engraving add-on: Rs. 500–800 (design pe depend karta hai)\n\n5+ orders pe special discount milta hai — message karen! 📩"
    },

    # ── ENGRAVING ────────────────────────────────────────
    {
        "keys": ["engrav", "personali", "custom", "name", "logo", "design", "laser", "khudaai", "naqsh"],
        "a": "Hamare engraving process ke steps:\n\n1️⃣ Tumbler choose karein (Owala ya Stanley)\n2️⃣ Batayein: Name / Text / Logo / Design\n3️⃣ Font style choose karein (10+ options hain)\n4️⃣ Position — front, back, ya dono\n5️⃣ Hum FREE mockup bhejte hain approval ke liye\n6️⃣ Confirm hone ke baad engrave karke ship karte hain!\n\nHum professional laser engraving use karte hain — permanent, scratch-resistant, aur bohot khoobsurat dikhti hai 🔥"
    },
    {
        "keys": ["font", "style", "text style", "font option", "likhawat"],
        "a": "Hum 10+ font styles offer karte hain:\n\n• Classic Serif\n• Modern Sans\n• Elegant Script / Cursive\n• Bold Block Letters\n• Minimalist Thin\n• Handwritten Style\n• Arabic Calligraphy ✨\n• Numbers & Symbols\n\nOrder karte waqt preferred style batayein ya reference image share karein. Hum match karenge! ✍️"
    },
    {
        "keys": ["kya engrave", "what to engrave", "kya likhwa", "kya likh sakte"],
        "a": "Aap almost kuch bhi engrave karwa sakte hain:\n\n✅ Naam ya nickname\n✅ Short quote ya phrase\n✅ Company/brand logo\n✅ Custom design ya artwork\n✅ Birth flower ya zodiac sign\n✅ QR code (businesses ke liye)\n✅ Monogram initials\n\n📌 Text limit: ~30 characters for clean results.\nLogos ke liye file share karein, hum check karenge!"
    },
    {
        "keys": ["mockup", "preview", "dekhna", "proof", "sample", "pehle dekh"],
        "a": "Haan! Hum hamesha FREE digital mockup bhejte hain engraving se pehle.\n\n📱 Aap exactly dekhenge design tumbler par kaisa lagega — placement, font, aur sizing ke saath.\n\nHum sirf aapki approval ke baad proceed karte hain. Koi surprise nahi! 👍"
    },

    # ── DELIVERY ─────────────────────────────────────────
    {
        "keys": ["deliver", "shipping", "ship", "dispatch", "how long", "when", "arrival", "receive", "kitne din", "kab milega", "courier"],
        "a": "Delivery time location pe depend karti hai:\n\n📦 Plain tumblers (engraving nahi):\n  • Karachi: 1–2 din\n  • Doosre cities: 3–5 din\n\n✏️ Engraved tumblers:\n  • Engraving + mockup approval ke liye 2–3 din extra\n  • Total: 3–7 din\n\nHum TCS / Leopards Courier se dispatch karte hain. Tracking number dispatch hone ke baad share kiya jaata hai! 🚚"
    },
    {
        "keys": ["karachi", "lahore", "islamabad", "peshawar", "quetta", "nationwide", "all cities", "pakistan", "poore pakistan", "har jagah"],
        "a": "Haan! Hum poore Pakistan mein deliver karte hain 🇵🇰\n\nShip karte hain:\n• Karachi, Lahore, Islamabad, Rawalpindi\n• Peshawar, Quetta, Multan, Faisalabad\n• Aur baaki sab cities\n\nShipping charges location pe depend karti hain. Rs. 5,000 se upar ke orders pe FREE delivery! 🎉"
    },

    # ── PAYMENT ──────────────────────────────────────────
    {
        "keys": ["payment", "pay", "cod", "cash", "bank", "easypaisa", "jazzcash", "online payment", "how to pay", "paise", "kaise dena"],
        "a": "Hum yeh payment methods accept karte hain:\n\n💵 Cash on Delivery (COD) — sirf Karachi mein\n\n🏦 Bank Transfer — Meezan Bank / HBL\n\n📱 EasyPaisa / JazzCash\n\n💳 Credit / Debit Card (online)\n\n📌 Note: Engraved orders ke liye 50% advance payment zaroori hai engraving shuru karne se pehle."
    },
    {
        "keys": ["advance", "deposit", "partial", "50%", "aadha paise"],
        "a": "Plain tumblers ke liye: Koi advance nahi (COD available in Karachi).\n\nEngraved tumblers ke liye: Haan, 50% advance shuru mein lena hota hai.\n\nYeh isliye hai kyunki engraving customized hoti hai aur resell nahi hoti. Baaqi 50% delivery pe dete hain 😊"
    },

    # ── RETURNS & WARRANTY ───────────────────────────────
    {
        "keys": ["return", "refund", "exchange", "policy", "warranty", "wapas", "dobara", "guarantee"],
        "a": "Haari policy:\n\n✅ Plain tumblers: 7-day return agar unused aur undamaged ho.\n\n❌ Engraved tumblers: Returns nahi (custom-made items). LEKIN agar hamari taraf se galti ya product defective ho, toh FREE replacement!\n\n📸 Damaged item mile toh turant photo lein aur 24 ghante ke andar contact karein.\n\nCustomer satisfaction hamare liye sab se zaroori hai 🙏"
    },
    {
        "keys": ["damage", "defect", "broken", "wrong", "mistake", "error", "kharab", "galat", "toota"],
        "a": "Maafi chahte hain agar aisa hua! Yeh karein:\n\n1. Issue ki clear photos lein\n2. Delivery ke 24 ghante ke andar contact karein\n3. Hum FREE replacement ya full refund arrange karenge\n\nHum apni galtion ki poori zimmedaari lete hain. Aapki satisfaction hamari priority hai! 💯"
    },

    # ── GIFTING ──────────────────────────────────────────
    {
        "keys": ["gift", "gifting", "present", "birthday", "wedding", "bridesmaid", "eid", "corporate", "bulk", "tohfa", "shaadi", "salgira"],
        "a": "Bilkul! Personalized tumblers BEST gifts hote hain 🎁\n\nHum offer karte hain:\n• Custom engraving with name/message\n• Gift wrapping (request pe)\n• Bulk gifting for events\n• 5+ orders pe special pricing\n\nPopular occasions:\n💍 Weddings & bridal showers\n🎂 Birthdays\n🏢 Corporate / employee gifting\n🌙 Eid gifts\n\nBulk quotes ke liye contact karein!"
    },
    {
        "keys": ["bulk", "wholesale", "multiple", "quantity", "order many", "large order", "zyada", "kaafi", "bahut saare"],
        "a": "Haan! Hum bulk orders love karte hain 🙌\n\nDiscounts:\n• 5–10 pieces: 10% off\n• 11–20 pieces: 15% off\n• 21+ pieces: 20% off\n\nCorporate logo engraving on bulk orders pe special rates!\n\nCustom quote ke liye WhatsApp/Instagram pe DM karein! 📩"
    },

    # ── HOW TO ORDER ─────────────────────────────────────
    {
        "keys": ["how to order", "place order", "order", "buy", "purchase", "kaise order", "kaise khareedna", "kaise lena", "order karna"],
        "a": "Order karna bilkul aasaan hai! 🚀\n\n1️⃣ WhatsApp ya Instagram pe message karein\n2️⃣ Batayein: Brand + Size + Color\n3️⃣ Engraving ke liye: name/design/font share karein\n4️⃣ Hum free mockup bhejte hain\n5️⃣ Confirm karein & payment karein\n6️⃣ Hum engrave karke dispatch karte hain!\n\n📲 WhatsApp: 0333-1234567\n📸 Instagram: @SaadEngraving"
    },

    # ── AUTHENTICITY ─────────────────────────────────────
    {
        "keys": ["original", "authentic", "real", "genuine", "fake", "asli", "nakli", "original product"],
        "a": "Haan, bilkul! 💯\n\nHamare Owala aur Stanley tumblers:\n✅ 100% authentic & original\n✅ Official distributors se sourced\n✅ Original packaging ke saath aate hain\n\nHum kabhi replicas nahi bechte. Agar kabhi non-authentic product mile — full refund guaranteed!"
    },

    # ── CARE INSTRUCTIONS ────────────────────────────────
    {
        "keys": ["care", "wash", "clean", "dishwasher", "maintain", "handle", "use", "saaf", "dhona", "rakhna"],
        "a": "Tumbler care tips:\n\n🧼 Cleaning:\n• Hand wash recommended\n• Owala lid dishwasher safe (top rack)\n• Stanley dishwasher safe\n• Bottle brush use karein andar ke liye\n• Harsh chemicals ya bleach avoid karein\n\n⚠️ Engraved tumblers ke liye:\n• Engraved area pe abrasive scrubbers use na karein\n• Hand wash preferred for long-lasting engraving\n\n🌡️ Microwave ya freeze mein mat rakhein!"
    },

    # ── CONTACT ──────────────────────────────────────────
    {
        "keys": ["contact", "reach", "whatsapp", "instagram", "social", "email", "number", "phone", "rabta", "kaise milein"],
        "a": "Hum se yahan contact karein:\n\n📲 WhatsApp: 0333-1234567\n(Mon–Sat, 10am–9pm)\n\n📸 Instagram: @SaadEngraving\n\n📧 Email: info@saadengraving.pk\n\nHum 1–2 ghante mein reply karte hain business hours mein. Urgent queries ke liye WhatsApp fastest hai! 💬"
    },

    # ── COLORS ───────────────────────────────────────────
    {
        "keys": ["color", "colour", "rang", "kaun se rang", "kaunsa color", "available colors"],
        "a": "Hum multiple colors mein available hain! 🎨\n\nOwala ke popular colors:\n• Tahoe (blue)\n• Lime\n• Candy Pink\n• Black\n• Teal\n\nStanley ke popular colors:\n• Cream\n• Charcoal\n• Rose Quartz\n• Alpine\n• Black\n\nLatest stock ke liye hamare Instagram @SaadEngraving check karein ya WhatsApp karein — colors stock pe depend karte hain! 📸"
    },
];

# ── GREETING & FALLBACK ──────────────────────────────────
GREETINGS = ["hi", "hello", "hey", "salam", "assalam", "aoa", "hye", "good morning", "good evening", "aslam", "walaikum"]
THANKS = ["thank", "shukriya", "thanks", "shukar", "mehrbani"]


def find_answer(text: str) -> str:
    t = text.lower()

    # Greeting check
    if any(t.startswith(g) for g in GREETINGS) or any(g in t for g in GREETINGS):
        return "Assalam o Alaikum! 👋 Saad Engraving mein aapka khoosh amdeed!\n\nMain aapki help kar sakta hoon Owala & Stanley tumblers, custom laser engraving, pricing, delivery aur bhi bohot kuch ke baare mein.\n\nKoi bhi sawaal poochein ya neeche quick questions mein se choose karein! 😊"

    # Thanks check
    if any(t_word in t for t_word in THANKS):
        return "Aap ka shukriya! 😊 Agar koi aur sawal ho toh zaroor poochein. Happy shopping! 🛍️"

    # Knowledge base matching
    best = None
    best_score = 0
    for item in KB:
        score = 0
        for key in item["keys"]:
            if key in t:
                score += len(key)
        if score > best_score:
            best_score = score
            best = item

    if best and best_score > 0:
        return best["a"]

    # Fallback
    return "Hmm, is sawaal ka jawab mujhe nahi pata! 🤔\n\nBehtar help ke liye seedha contact karein:\n\n📲 WhatsApp: 0333-1234567\n📸 Instagram: @SaadEngraving\n\nHum zaroor aapki help karenge! 💬"


# ── ROUTES ───────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_msg = data.get("message", "").strip()
    if not user_msg:
        return jsonify({"reply": "Kuch toh likhen! 😊"})
    reply = find_answer(user_msg)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
