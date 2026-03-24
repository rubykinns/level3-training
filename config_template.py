# =============================================================================
# config.py — Level 3 Automation Driver Training
# Based on: Level3_Driver_Training.pptx
#
# SCRIPTED_TOPICS  : Group 3 fixed chatbot script (same for every participant)
# TRAINING_TOPICS  : Group 4 AI conversation content (Group A/B versions)
# QUIZ_QUESTIONS   : Post-training quiz (same for all groups)
# STRUCTURED_FEEDBACK : Group 3 post-quiz feedback (Group A/B versions)
# CHATBOT_SYSTEM_PROMPT : AI instructor behavior for Group 4
# =============================================================================

ANTHROPIC_API_KEY = ""
MODEL = "claude-haiku-4-5-20251001"
import base64

def img_to_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

gray_img   = img_to_base64("gray.png")
green_img  = img_to_base64("green.png")
yellow_img = img_to_base64("yellow.png")
red_img    = img_to_base64("red.png")
# =============================================================================
# SCRIPTED TOPICS — Group 3 ONLY
# Fixed script — every participant sees exactly the same messages.
# 5 modules mirroring the PPT structure.
#
# Each step:
#   "message"      : AI instructor message
#   "yes_followup" : response when participant understands (optional)
#   "no_followup"  : response when participant types confusion keywords
#
# Confusion keywords: "no", "again", "explain", "unclear",
#                     "confused", "confusing", "help", "don't", "didn't", "not"
# All other input → advance to next step
# =============================================================================

SCRIPTED_TOPICS = [

    # ── MODULE 1: Core Concepts ───────────────────────────────────────────────
    {
        "title": "Module 1: Core Concepts of Level 3 Automation",
        "steps": [
            {
                "message": (
                    "Welcome to your <b>Level 3 Automation Driver Training!<b> 🚗\n\n"
                    "Let's start with a quick overview of SAE automation levels. "
                    "Take a look at the diagram below — it shows all six levels defined by SAE International J3016:\n\n"
                    "**Level 0 — No Automation**\n"
                    "Full and constant responsibility for all dynamic driving tasks. No system support. The driver is the human operator.\n\n"
                    "**Level 1 — Driver Assistance**\n"
                    "The vehicle features a single automated system (e.g. speed or steering control). "
                    "Driver must monitor and adjust continuously. Supervised control.\n\n"
                    "**Level 2 — Partial Automation**\n"
                    "The vehicle can perform steering and acceleration. "
                    "Driver must monitor continuously and take control at any time. Combined monitoring.\n\n"
                    "**Level 3 — Conditional Automation** (**Today's focus**)\n"
                    "The vehicle can perform most driving tasks under specific conditions. "
                    "Driver is NOT responsible for monitoring, but MUST be ready to take over on request. Fallback ready.\n\n"
                    "**Level 4 — High Automation**\n"
                    "The vehicle handles all driving tasks under most conditions autonomously. "
                    "Minimal intervention might be necessary. Limited use.\n\n"
                    "**Level 5 — Full Automation**\n"
                    "The vehicle handles all driving tasks under all conditions autonomously. "
                    "No driver responsibility for any aspect of the dynamic driving task. No driver required.\n\n"
                    "Does this overview of SAE levels make sense to you? Click the image to enlarge."
                ),
                "image": "Sae levels.png",
                "yes_followup": "Great! Let's look at what Level 3 specifically means for you as a driver.",
                "no_followup": (
                    "No problem! Here's the key difference to focus on:\n\n"
                    "At Level 2, you must always watch the road — even if the car is steering.\n"
                    "At Level 3, the system monitors the environment for you — but only in certain conditions, "
                    "and you must be ready to step in when it asks.\n\n"
                    "Think of it as: Level 2 = co-pilot who watches, Level 3 = pilot who occasionally needs backup.\n\n"
                    "Does that help clarify the difference?"
                ),
            },
            {
                "message": (
                    "So what exactly is <b>Level 3 — Conditional Automation</b>?<br><br>"
                    "🤖 <b>The system takes the wheel:</b> <br><br>"
                    "The vehicle <b>steers, accelerates, and brakes</b> on its own. "
                    "The system monitors the environment — not you.<br><br>"
                    "⚠️ <b>Conditional, not full automation:</b> <br><br>"
                    "It only works within a **specific Operational Design Domain (ODD)** — "
                    "defined road types, speed ranges, and weather conditions set by the manufacturer.<br><br>"
                    "🔄 <b>Takeover is your responsibility</b>:<br><br>"
                    "When the system **reaches its limits**, it issues a **Takeover Request (ToR)**. "
                    "You **MUST** respond promptly.\n\n"
                    "Does this definition of Level 3 make sense to you?"
                ),
                "yes_followup": None,
                "no_followup": (
                    "Let's simplify to three rules:\n\n"
                    "1. The car drives — but only under specific conditions.\n"
                    "2. You don't need to stare at the road, but stay available.\n"
                    "3. When the car asks for you → take over immediately.\n\n"
                    "That's the core of Level 3. Ready to continue?"
                ),
            },
            {
                "message": (
                    "<b>A key distinction: Level 2 vs. Level 3.<b>\n\n"
                    "<table style='width:100%; border-collapse:collapse; font-size:14px; margin:10px 0;'>"
                    "<thead>"
                    "<tr style='background:#1d4ed8; color:white;'>"
                    "<th style='padding:10px; text-align:left;'>Aspect</th>"
                    "<th style='padding:10px; text-align:center;'>Level 2<br><span style='font-weight:400; font-size:12px;'>Partial Automation</span></th>"
                    "<th style='padding:10px; text-align:center; background:#1e40af;'>Level 3 <br><span style='font-weight:400; font-size:12px;'>Conditional Automation</span></th>"
                    "</tr>"
                    "</thead>"
                    "<tbody>"
                    "<tr style='background:#f8f9fb;'>"
                    "<td style='padding:10px; font-weight:600;'>Who monitors the road?</td>"
                    "<td style='padding:10px; text-align:center;'>Driver — always</td>"
                    "<td style='padding:10px; text-align:center; color:#1d4ed8; font-weight:600;'>System (within ODD)</td>"
                    "</tr>"
                    "<tr style='background:#ffffff;'>"
                    "<td style='padding:10px; font-weight:600;'>Eyes off road allowed?</td>"
                    "<td style='padding:10px; text-align:center;'>❌ No</td>"
                    "<td style='padding:10px; text-align:center; color:#1d4ed8; font-weight:600;'>✅ Yes — temporarily</td>"
                    "</tr>"
                    "<tr style='background:#f8f9fb;'>"
                    "<td style='padding:10px; font-weight:600;'>Driving responsibility</td>"
                    "<td style='padding:10px; text-align:center;'>Driver — always</td>"
                    "<td style='padding:10px; text-align:center; color:#1d4ed8; font-weight:600;'>System → transitions to Driver</td>"
                    "</tr>"
                    "<tr style='background:#ffffff;'>"
                    "<td style='padding:10px; font-weight:600;'>Takeover Request (TOR)?</td>"
                    "<td style='padding:10px; text-align:center;'>Not applicable</td>"
                    "<td style='padding:10px; text-align:center; color:#1d4ed8; font-weight:600;'>Yes — must respond</td>"
                    "</tr>"
                    "<tr style='background:#f8f9fb;'>"
                    "<td style='padding:10px; font-weight:600;'>Non-driving tasks OK?</td>"
                    "<td style='padding:10px; text-align:center;'>❌ No</td>"
                    "<td style='padding:10px; text-align:center; color:#1d4ed8; font-weight:600;'>✅ Yes — with restrictions</td>"
                    "</tr>"
                    "</tbody>"
                    "</table>"
                    "<br>Is this difference between Level 2 and Level 3 clear?"
                ),
                
                "yes_followup": "Good. Now let's talk about <b>your responsibilities<b> as the driver during Level 3.",
                "no_followup": (
                    "Here's the simplest way to remember it:\n\n"
                    "**Level 2** = Hands-off, but EYES ON the road at all times.\n\n"
                    "**Level 3** = Eyes can be off the road, but BE READY to take over.\n\n"
                    "That one difference is what makes Level 3 a significant step forward — "
                    "and why understanding your responsibilities matters so much. Clear now?"
                ),
            },
            {
                "message": (
                    "Here's what you <b>ARE</b> responsible for during Level 3 automation:<br><br>"
                    "💺 <b>Stay in the driver's seat at all times</b> — You must remain in the driver's seat and within reach of the steering wheel at all times.\n\n"
                    "🚨 **Be physically able to resume control and stay alert** — Do not drive tired, impaired, or medicated.\n\n"
                    "🖐️ **Hands and feet ready when alerted** — When a Takeover Request is issued, place hands on the wheel and feet near the pedals.\n\n"
                    "⚡ **Respond to every Takeover Request** — You must take over when the system alerts you for either planned or urgent. Never dismiss or delay. \n\n"
                    "📊 **Monitor the dashboard every 30–60 seconds** — "
                    "Green =  active, Yellow = prepare, Red = act now.\n\n"
                    "Does this list of driver responsibilities make sense?"
                ),
                "yes_followup": "Good. Now let's look at what you should <b>NOT</b> do during Level 3.",
                "no_followup": (
                    "Think of it this way — Level 3 reduces your workload, but does <b>NOT</b> eliminate your role.\n\n"
                    "You still need to:\n\n"
                    "• Stay in the seat\n\n"
                    "• Stay awake and capable\n\n"
                    "• Respond to alerts\n\n"
                    "• Glance at the dashboard occasionally\n\n"
                    "The system drives. You remain the responsible backup. Does that make sense?"
                ),
            },
            {
                "message": (
                    "And here's what you should <b>NOT</b> do while Level 3 automation is active:<br><br>"
                    "😴 <b>Sleep or become fully unresponsive</b> — Drowsy drivers need more response time to react compared to drivers who are alert.<br><br>"
                    "💺 <b>Leave the driver's seat</b> — You must remain within reach of the steering wheel at all times during automation..\n\n"
                    "❗️ <b>Ignore or dismiss a TOR alert</b> — You must takeover if you receive a ToR request.\n\n"
                    "🍺 <b>Drive under the influence</b> — Alcohol, drugs, or impairing medication are prohibited regardless of automation level.\n\n"
                    "⏳ <b>Engage in tasks you can't stop immediately</b> — Only do things you can interrupt within seconds.\n\n"
                    "Does this list of prohibited behaviors make sense?"
                ),
                "yes_followup": (
                    "Great! You've completed <b>Module 1</b>. 🎉<br><br>"
                    "Let's move on to <b>Module 2: Operational Design Domains</b> — "
                    "the specific conditions under which Level 3 can and cannot operate."
                ),
                "no_followup": (
                    "The key rule is: only do things you can <b>STOP</b> within a few seconds.\n\n"
                    "<b>Phone call?</b> OK — you can put it down.\n\n"
                    "<b>Watching a movie?</b> Not OK — you'll be too absorbed.\n\n"
                    "<b>Napping?</b> Definitely not — you won't hear the ToR alert.\n\n"
                    "Level 3 gives you a break from driving, not from being a driver. Ready to continue?"
                ),
            },
        ],
    },

    # ── MODULE 2: Operational Design Domain ──────────────────────────────────
    {
        "title": "<b>Module 2: Operational Design Domains (ODD)<b> <br><br>",
        "steps": [
            {
                "message": (
                    "Module 2: <b>Operational Design Domains (ODD)</b><br><br>"
                    "The ODD defines the <b>specific conditions</b> under which a Level 3 system is designed to function safely.<br><br>"
                    "<ul style='margin:8px 0; padding-left:20px;'>"
                    "🗂️ <b>System Boundary</b> <br><br>"
                    "Important points:\n\n"
                    "<li>The ODD is defined by the manufacturer — not you.</li>"
                    "<li>Each vehicle model has its own documented ODD.</li>"
                    "</ul>"
                    "⚠️ <b>Outside ODD = Unreliable</b>"
                    "<ul style='margin:8px 0; padding-left:20px;'>"
                    "<li>ODD is defined by the manufacturer, not the driver.</li>"
                    "<li>Each vehicle model has its own documented ODD — it defines where the system is permitted to operate.</li>"
                    "<li>Outside these conditions, the system may not operate reliably and will request driver takeover.</li>"
                    "<li>Ignoring this boundary is unsafe.</li>"
                    "</ul>"
                    "💡 ODD defines the system's <b>boundary</b> — not its capability. Safe use starts with understanding this distinction.<br><br>"
                    "<b>Does the concept of ODD make sense?</b>"
                ),

                "yes_followup": "Good. Let's look at the four ODD condition categories.",
                "no_followup": (
                    "Think of ODD like the operating manual for an appliance:<br><br>"
                    "A washing machine is designed for clothes — not bricks. "
                    "It might handle one brick, but it's not built for it and could break.\n\n"
                    "Similarly, Level 3 is designed for specific road conditions. "
                    "Outside those, it can't guarantee safe operation.\n\n"
                    "The manufacturer defines exactly what those conditions are. Does that explanation help?"
                ),
            },
            {
                "message": (
                    "ODD is defined by <b>four condition</b> categories — ALL must be met simultaneously:\n\n"
                    "🛣️ <b>01. Road Type & Geometry</b> \n\n"
                    "🚗 <b>02. Traffic Conditions</b> \n\n"
                    "🌤️ <b>03. Environmental Conditions</b> \n\n"
                    "🗺️ <b>04. Geographic Area & Map</b> <br><br>"
                    
                    "⚠️ **All Four conditions must be satisfied simultaneously.** \n\n **Failure of even one category** can cause the system to issue a Takeover Request — even if all other conditions are fine.\n\n"
                    "Does this **four condition categories** make sense?"
                ),
                "yes_followup": "Good. Let's go through each category in more detail.",
                "no_followup": (
                    "Think of it like a checklist before activation:\n\n"
                    "✅ Road type OK?\n\n"
                    "✅ Traffic OK?\n\n"
                    "✅ Weather OK?\n\n"
                    "✅ GPS & map OK?\n\n"
                    "If even one item on that checklist fails, the system exits automation. "
                    "All four must be green at the same time. Does that make it clearer?"
                ),
            },
    
            {
                "message": (
                    "Let's look at each ODD category in detail.\n\n"
                    "<table style='width:100%; border-collapse:collapse; font-size:14px; margin:10px 0;'>"
                    "<thead>"
                    "<tr style='background:#1d4ed8; color:white;'>"
                    "<th style='padding:10px; text-align:left;'>Category</th>"
                    "<th style='padding:10px; text-align:left;'>✅ Within ODD</th>"
                    "<th style='padding:10px; text-align:left;'>🚫 Outside ODD</th>"
                    "</tr>"
                    "</thead>"
                    "<tbody>"
                    "<tr style='background:#f8f9fb;'>"
                    "<td style='padding:10px; font-weight:600;'>🛣️ Roadway</td>"
                    "<td style='padding:10px;'><ul style='margin:0; padding-left:16px;'>"
                    "<li>Divided highways</li>"
                    "<li>Limited-access roads</li>"
                    "<li>Clear lane markings</li>"
                    "<li>Predictable geometry</li>"
                    "</ul></td>"

                    "<td style='padding:10px;'><ul style='margin:0; padding-left:16px;'>"
                    "<li>Urban streets</li>"
                    "<li>Roundabouts &amp; school zones</li>"
                    "<li>Construction-altered roads</li>"
                    "<li>Unmarked rural roads</li>"
                    "</ul></td>"
                    "<tr style='background:#ffffff;'>"
                    "<td style='padding:10px; font-weight:600;'>🚗 Traffic</td>"
                    "<td style='padding:10px;'><ul style='margin:0; padding-left:16px;'>"
                    "<li>Moderate highway flow</li>"
                    "<li>Stop-and-go within speed range</li>"
                    "<li>Limited pedestrians/cyclists</li>"
                    "</ul></td>"
                    "<td style='padding:10px;'><ul style='margin:0; padding-left:16px;'>"
                    "<li>Frequent cut-ins</li>"
                    "<li>Dense or chaotic traffic</li>"
                    "<li>Cyclists &amp; pedestrians</li>"
                    "<li>Emergency vehicles nearby</li>"
                    "</ul></td>"
                    "</tr>"
                    "</tbody>"
                    "</table>"
                    "<br>💡 <b>Road type</b> is the most common reason Level 3 disengages — always check your route before activating.<br>"
                    "💡 Even within ODD, high <b>traffic complexity</b> can trigger an urgent TOR — stay alert in dense traffic.<br><br>"
                    "Is this clear so far?"
                ),
                "yes_followup": "Good. Let's look at <b>environmental and geographic conditions.</b>",
                "no_followup": (
                    "Here's the simple version:\n\n"
                    "Road type → Highways YES, city streets NO.\n"
                    "Traffic → Predictable flow YES, chaotic or unpredictable NO.\n\n"
                    "If you're on a highway with steady traffic, you're likely within ODD for these two categories. "
                    "Ready to continue with the other two?"
                ),
            },
            {
                "message": (
                    "<table style='width:100%; border-collapse:collapse; font-size:14px; margin:10px 0;'>"
                    "<thead>"
                    "<tr style='background:#1d4ed8; color:white;'>"
                    "<th style='padding:10px; text-align:left;'>Category</th>"
                    "<th style='padding:10px; text-align:left;'>✅ Within ODD</th>"
                    "<th style='padding:10px; text-align:left;'>🚫 Outside ODD</th>"
                    "</tr>"
                    "</thead>"
                    "<tbody>"
                    "<tr style='background:#f8f9fb;'>"
                    "<td style='padding:10px; font-weight:600;'>🌤️ Environmental</td>"
                    "<td style='padding:10px;'><ul style='margin:0; padding-left:16px;'>"
                    "<li>Clear sky or light overcast</li>"
                    "<li>Daylight or well-lit roads</li>"
                    "<li>Light rain</li>"
                    "<li>Dry road surface</li>"
                    "</ul></td>"
                    "<td style='padding:10px;'><ul style='margin:0; padding-left:16px;'>"
                    "<li>Heavy rain or snow</li>"
                    "<li>Dense fog</li>"
                    "<li>Low-angle direct sunlight</li>"
                    "<li>Ice, mud, or sensor blockage</li>"
                    "</ul></td>"
                    "</tr>"
                    "</tr>"
                    "<tr style='background:#ffffff;'>"
                    "<td style='padding:10px; font-weight:600;'>🗺️ Geographical</td>"
                    "<td style='padding:10px;'><ul style='margin:0; padding-left:16px;'>"
                    "<li>Pre-mapped road segments</li>"
                    "<li>Centimeter-level GPS available</li>"
                    "<li>Manufacturer-approved regions</li>"
                    "<li>Up-to-date HD map data</li>"
                    "</ul></td>"
                    "<td style='padding:10px;'><ul style='margin:0; padding-left:16px;'>"
                    "<li>Tunnels (GPS loss)</li>"
                    "<li>Dense urban canyons</li>"
                    "<li>Unmapped or new roads</li>"
                    "<li>Unapproved geographic regions</li>"
                    "</ul></td>"
                    "</tr>"
                    "</tbody>"
                    "</table>"
                    "<br>⚠️ <b>Sensors may degrade without warning</b> — always check weather before a trip and monitor conditions during automation.<br>"
                    "💡 <b>Proactive tip:</b> Check your route for tunnels and unsupported roads before activating Level 3.<br><br>"
                    "Does this complete picture of ODD conditions make sense?"
                ),
                "yes_followup": (
                    "Excellent! You've completed <b>Module 2</b>. 🎉<br><br>"
                    "Next up: <b>Module 3 — Takeover Requests.</b> "
                    "This is the most critical skill in Level 3 driving."
                ),
                "no_followup": (
                    "Here's the short version for <b>environmental and geographic conditions</b>:\n\n"
                    "Environment → Good visibility and weather YES, fog/snow/ice NO.\n"
                    "Geography → Mapped highways with GPS YES, tunnels/unmapped roads/unsupported regions NO.\n\n"
                    "When in doubt about any of these conditions — don't activate Level 3. "
                    "Manual control is always the safe choice. Does that make sense?"
                ),
            },
        ],
    },

    # ── MODULE 3: Takeover Requests ───────────────────────────────────────────
    {
        "title": "Module 3: Takeover Requests (ToR)",
        "steps": [
            {
                "message": (
                    "<b>Module 3: Takeover Requests — The Most Critical Skill </b>🚨<br><br>"
                    "<b>A Takeover Request (ToR)</b> is the system's signal: "
                    "\"<b>I cannot continue safely — please take manual control now.</b>\"\n\n"
                    "<b>ToR alerts come in three forms</b> — often simultaneously:<br><br>"
                    "<div style='display:flex; gap:10px; margin:8px 0;'>"

                    "<div style='flex:1; background:#eff6ff; border:1px solid #bfdbfe; border-radius:10px; padding:14px; text-align:center;'>"
                    "<div style='font-size:28px; margin-bottom:8px;'>👁️</div>"
                    "<div style='font-weight:700; color:#1d4ed8; margin-bottom:6px;'>Visual</div>"
                    "<div style='font-size:13px; color:#374151;'>Dashboard flashes with a warning icon</div>"
                    "</div>"

                    "<div style='flex:1; background:#eff6ff; border:1px solid #bfdbfe; border-radius:10px; padding:14px; text-align:center;'>"
                    "<div style='font-size:28px; margin-bottom:8px;'>🔊</div>"
                    "<div style='font-weight:700; color:#1d4ed8; margin-bottom:6px;'>Audible</div>"
                    "<div style='font-size:13px; color:#374151;'>Repeated alarm tones — escalate the longer you wait</div>"
                    "</div>"

                    "<div style='flex:1; background:#eff6ff; border:1px solid #bfdbfe; border-radius:10px; padding:14px; text-align:center;'>"
                    "<div style='font-size:28px; margin-bottom:8px;'>📳</div>"
                    "<div style='font-weight:700; color:#1d4ed8; margin-bottom:6px;'>Haptic</div>"
                    "<div style='font-size:13px; color:#374151;'>Seat vibrates and/or steering wheel pulses</div>"
                    "</div>"

                    "</div><br>"
                    "The alerts get more intense over time — the system is designed to get your attention no matter what.\n\n"
                    "Have you ever seen or experienced a driver alert system in a vehicle before?"
                ),
                "yes_followup": "Good — this will feel familiar then. The stakes with TOR are just higher.",
                "no_followup": (
                    "Think of a TOR like a fire alarm:\n\n"
                    "It doesn't necessarily mean disaster — it means act now.\n"
                    "The alarm gets louder if you don't respond, just like a fire alarm escalates.\n\n"
                    "Your job is simply to respond promptly and take control. "
                    "We'll walk through exactly how to do that next. Ready?"
                ),
            },
            {
                "message": (
                    "When a TOR is issued, execute these 6 steps in order:\n\n"
                    "<div style='display:flex; flex-direction:column; gap:8px; margin:8px 0;'>"

                    "<div style='display:flex; align-items:flex-start; gap:12px; background:#f8f9fb; border:1px solid #e5e7eb; border-radius:10px; padding:12px;'>"
                    "<div style='background:#1d4ed8; color:white; border-radius:50%; width:28px; height:28px; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:13px; flex-shrink:0;'>1</div>"
                    "<div><div style='font-weight:700; color:#1d4ed8;'>Eyes to Road</div>"
                    "<div style='font-size:13px; color:#374151;'>Immediately look up and assess — where is traffic? What's ahead?</div></div>"
                    "</div>"

                    "<div style='display:flex; align-items:flex-start; gap:12px; background:#f8f9fb; border:1px solid #e5e7eb; border-radius:10px; padding:12px;'>"
                    "<div style='background:#1d4ed8; color:white; border-radius:50%; width:28px; height:28px; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:13px; flex-shrink:0;'>2</div>"
                    "<div><div style='font-weight:700; color:#1d4ed8;'>Hands on Wheel</div>"
                    "<div style='font-size:13px; color:#374151;'>Both hands firmly on. Don't wait until you understand the situation.</div></div>"
                    "</div>"

                    "<div style='display:flex; align-items:flex-start; gap:12px; background:#f8f9fb; border:1px solid #e5e7eb; border-radius:10px; padding:12px;'>"
                    "<div style='background:#1d4ed8; color:white; border-radius:50%; width:28px; height:28px; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:13px; flex-shrink:0;'>3</div>"
                    "<div><div style='font-weight:700; color:#1d4ed8;'>Stabilize Lane</div>"
                    "<div style='font-size:13px; color:#374151;'>Maintain your lane position smoothly. No sudden steering.</div></div>"
                    "</div>"

                    "<div style='display:flex; align-items:flex-start; gap:12px; background:#f8f9fb; border:1px solid #e5e7eb; border-radius:10px; padding:12px;'>"
                    "<div style='background:#1d4ed8; color:white; border-radius:50%; width:28px; height:28px; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:13px; flex-shrink:0;'>4</div>"
                    "<div><div style='font-weight:700; color:#1d4ed8;'>Assess Surroundings</div>"
                    "<div style='font-size:13px; color:#374151;'>Check mirrors, blind spots, and what triggered the TOR.</div></div>"
                    "</div>"

                    "<div style='display:flex; align-items:flex-start; gap:12px; background:#f8f9fb; border:1px solid #e5e7eb; border-radius:10px; padding:12px;'>"
                    "<div style='background:#1d4ed8; color:white; border-radius:50%; width:28px; height:28px; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:13px; flex-shrink:0;'>5</div>"
                    "<div><div style='font-weight:700; color:#1d4ed8;'>Apply Brake / Acceleration</div>"
                    "<div style='font-size:13px; color:#374151;'>React to the road situation and adjust speed as needed.</div></div>"
                    "</div>"

                    "<div style='display:flex; align-items:flex-start; gap:12px; background:#f8f9fb; border:1px solid #e5e7eb; border-radius:10px; padding:12px;'>"
                    "<div style='background:#1d4ed8; color:white; border-radius:50%; width:28px; height:28px; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:13px; flex-shrink:0;'>6</div>"
                    "<div><div style='font-weight:700; color:#1d4ed8;'>Confirm Full Manual Control</div>"
                    "<div style='font-size:13px; color:#374151;'>Verify automation is OFF on the HMI. You are now in control.</div></div>"
                    "</div>"

                    "</div><br>"
                    "Does this <b>6-step TOR response process</b> make sense?"
                ),
                "yes_followup": "Good. Now let's look at the three different types of TOR.",
                "no_followup": (
                    "Let's simplify to the first three steps — the most critical ones:\n\n"
                    "Step 1: Look at the road.\n\n"
                    "Step 2: Grab the wheel.\n\n"
                    "Step 3: Don't swerve — stabilize first.\n\n"
                    "Steps 4-6 follow naturally once you're in control. "
                    "The key is: eyes and hands first, assessment second. Clear?"
                ),
            },
            {
                "message": (
                    "There are three types of ToR — each requires a different response speed:\n\n"
                    "<div style='display:flex; flex-direction:column; gap:10px; margin:8px 0;'>"

                    # Planned TOR - Green
                    "<div style='background:#f0fdf4; border:1px solid #86efac; border-left:4px solid #22c55e; border-radius:10px; padding:14px;'>"
                    "<div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;'>"
                    "<div style='font-weight:700; color:#15803d; font-size:15px;'>1️⃣ PLANNED ToR</div>"
                    "<div style='background:#22c55e; color:white; border-radius:99px; padding:2px 10px; font-size:12px; font-weight:600;'>25–30 sec</div>"
                    "</div>"
                    "<div style='font-size:13px; color:#374151; margin-bottom:8px;'>System detects an upcoming ODD boundary (e.g., highway exit, construction ahead). Most manageable type.</div>"
                    "<div style='background:#dcfce7; border-radius:6px; padding:8px; font-size:13px; color:#15803d;'>"
                    "✅ Wrap up task → Eyes on road → Hands on wheel → Accept control early"
                    "</div>"
                    "</div>"

                    # Urgent TOR - Orange
                    "<div style='background:#fff7ed; border:1px solid #fdba74; border-left:4px solid #f97316; border-radius:10px; padding:14px;'>"
                    "<div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;'>"
                    "<div style='font-weight:700; color:#c2410c; font-size:15px;'>2️⃣ URGENT ToR</div>"
                    "<div style='background:#f97316; color:white; border-radius:99px; padding:2px 10px; font-size:12px; font-weight:600;'>4–7 sec</div>"
                    "</div>"
                    "<div style='font-size:13px; color:#374151; margin-bottom:8px;'>Unexpected event — sudden road condition change, sensor issue, traffic emergency. Strong alerts: beeps + seat vibration.</div>"
                    "<div style='background:#ffedd5; border-radius:6px; padding:8px; font-size:13px; color:#c2410c;'>"
                    "✅ Drop everything immediately → Eyes on road → Hands on wheel → Assess and react"
                    "</div>"
                    "</div>"

                    # Failure TOR - Red
                    "<div style='background:#fef2f2; border:1px solid #fca5a5; border-left:4px solid #ef4444; border-radius:10px; padding:14px;'>"
                    "<div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;'>"
                    "<div style='font-weight:700; color:#dc2626; font-size:15px;'>3️⃣ FAILURE ToR</div>"
                    "<div style='background:#ef4444; color:white; border-radius:99px; padding:2px 10px; font-size:12px; font-weight:600;'>Critical</div>"
                    "</div>"
                    "<div style='font-size:13px; color:#374151; margin-bottom:8px;'>Vehicle initiates Minimal Risk Condition (MRC) automatically — slows and stops safely.</div>"
                    "<div style='background:#fee2e2; border-radius:6px; padding:8px; font-size:13px; color:#dc2626;'>"
                    "✅ Take control ASAP. If unable — assist MRC. Steer to shoulder when safe."
                    "</div>"
                    "</div>"

                    "</div><br>"
                    "Does understanding the <b>three types of ToR</b> make sense?"
                ),
                "yes_followup": (
                    "Great! You've completed <b>Module 3</b>. 🎉\n\n"
                    "<b>Module 4</b> covers <b>How the System Works</b> — specifically, the dashboard signals "
                    "that tell you what mode the system is in."
                ),
                "no_followup": (
                    "Here's the key takeaway for each type:\n\n"
                    "Planned ToR → You have time. Wrap up and take over smoothly.\n"
                    "Urgent ToR → No time. Drop everything and react immediately.\n"
                    "Failure ToR → System is stopping the car. Help it if you can.\n\n"
                    "The common thread: always take ToR alerts seriously, every single time. Ready to continue?"
                ),
            },
        ],
    },

    # ── MODULE 4: How the System Works ───────────────────────────────────────
    {
        "title": "Module 4: How the System Works — HMI Signals",
        "steps": [
            {
                "message": (
                    
                    "<b>Module 4: How the System Works — Reading Your Dashboard</b> 📊<br><br>"
                    "Your <b>Human-Machine Interface (HMI)</b> is your window into what the system is doing. "
                    "There are four dashboard states you need to know:<br><br>"

                    "<div style='display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:8px 0;'>"

                    # GREEN
                    "<div style='background:#f0fdf4; border:2px solid #22c55e; border-radius:10px; padding:14px; text-align:center;'>"
                    f"<img src='data:image/png;base64,{green_img}' style='width:100%; border-radius:6px; margin-bottom:8px;'>"
                    "<div style='font-weight:700; color:#15803d; font-size:15px; margin-bottom:4px;'>🟢 GREEN — System Active</div>"
                    "<div style='font-size:13px; color:#374151;'>Automation fully engaged. You may engage in permitted non-driving tasks.</div>"
                    "</div>"

                    # YELLOW
                    "<div style='background:#fefce8; border:2px solid #eab308; border-radius:10px; padding:14px; text-align:center;'>"
                    f"<img src='data:image/png;base64,{yellow_img}' style='width:100%; border-radius:6px; margin-bottom:8px;'>"
                    "<div style='font-weight:700; color:#a16207; font-size:15px; margin-bottom:4px;'>🟡 YELLOW — Prepare to Take Over</div>"
                    "<div style='font-size:13px; color:#374151;'>Approaching ODD boundary. Wrap up tasks and prepare for manual control.</div>"
                    "</div>"

                    # RED
                    "<div style='background:#fef2f2; border:2px solid #ef4444; border-radius:10px; padding:14px; text-align:center;'>"
                    f"<img src='data:image/png;base64,{red_img}' style='width:100%; border-radius:6px; margin-bottom:8px;'>"
                    "<div style='font-weight:700; color:#dc2626; font-size:15px; margin-bottom:4px;'>🔴 RED — Take Over NOW</div>"
                    "<div style='font-size:13px; color:#374151;'>Drop everything. Hands on wheel. Eyes on road. Act within seconds.</div>"
                    "</div>"

                    # GRAY
                    "<div style='background:#f9fafb; border:2px solid #9ca3af; border-radius:10px; padding:14px; text-align:center;'>"
                    f"<img src='data:image/png;base64,{gray_img}' style='width:100%; border-radius:6px; margin-bottom:8px;'>"
                    "<div style='font-weight:700; color:#4b5563; font-size:15px; margin-bottom:4px;'>⚫ GRAY — System Not Active</div>"
                    "<div style='font-size:13px; color:#374151;'>Automation unavailable. Drive fully manually.</div>"
                    "</div>"

                    "</div><br>"
                    "Does the <b>four-color HMI system</b> make sense?"
                    ),
                "yes_followup": (
                    "Excellent! You've completed <b>Module 4</b>. 🎉<br><br>"
                    "One more module to go — <b>Module 5 covers Driver Issues.</b> "
                    
                ),
                "no_followup": (
                    "Think of it like a traffic light — but for your automation system:\n\n"
                    "🟢 Green = Go. System is driving. You're fine.\n\n"
                    "🟡 Yellow = Caution. Get ready to take over soon.\n"
                    "🔴 Red = Stop (everything else). Take over RIGHT NOW.\n"
                    "⚫ Gray = No signal. Drive manually.\n\n"
                    "Glancing at the HMI every 30–60 seconds keeps you aware of the system's status. Clear?"
                ),
            
            },
        ],
    },

    # ── MODULE 5: Driver Issues ───────────────────────────────────────────────
    {
        "title": "Module 5: The Driver Issues — Overtrust, Complacency, Mode Confusion",
        "steps": [
            {
                "message": (
                    "<b>Module 5: The Driver Issues</b> 🧠<br><br>"
                    "Research shows that most Level 3-related incidents are caused by <b>driver behavior</b> — "
                    "not system failure. There are three behavioral traps to be aware of:<br><br>"

                    "<div style='display:flex; flex-direction:column; gap:10px; margin:8px 0;'>"

                    # Trap 1
                    "<div style='background:#fffbeb; border:1px solid #fcd34d; border-left:4px solid #f59e0b; border-radius:10px; padding:14px;'>"
                    "<div style='font-weight:700; color:#92400e; font-size:15px; margin-bottom:6px;'>😌 Trap 1 — Over-Trust (Automation Bias)</div>"
                    "<div style='font-style:italic; color:#78350f; background:#fef3c7; border-radius:6px; padding:8px; margin-bottom:8px; font-size:13px;'>"
                    "\"The system handles everything. I don't need to stay alert.\""
                    "</div>"
                    "<div style='font-size:13px; color:#374151;'>⚠️ <b>Risk:</b> When the system hits its limits, you won't be ready to take over in time.</div>"
                    "</div>"

                    # Trap 2
                    "<div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:4px solid #1d4ed8; border-radius:10px; padding:14px;'>"
                    "<div style='font-weight:700; color:#1d4ed8; font-size:15px; margin-bottom:6px;'>😶 Trap 2 — Complacency (Out-of-the-Loop)</div>"
                    "<div style='font-style:italic; color:#1e40af; background:#dbeafe; border-radius:6px; padding:8px; margin-bottom:8px; font-size:13px;'>"
                    "\"Nothing has gone wrong in weeks, so nothing will today.\""
                    "</div>"
                    "<div style='font-size:13px; color:#374151;'>⚠️ <b>Risk:</b> After 60+ minutes of automation, TOR response times can be 2–3x slower than at trip start.</div>"
                    "</div>"

                    # Trap 3
                    "<div style='background:#fffbeb; border:1px solid #fcd34d; border-left:4px solid #f59e0b; border-radius:10px; padding:14px;'>"
                    "<div style='font-weight:700; color:#92400e; font-size:15px; margin-bottom:6px;'>😵 Trap 3 — Mode Confusion</div>"
                    "<div style='font-style:italic; color:#78350f; background:#fef3c7; border-radius:6px; padding:8px; margin-bottom:8px; font-size:13px;'>"
                    "\"Wait — is the car in auto mode right now or not?\""
                    "</div>"
                    "<div style='font-size:13px; color:#374151;'>⚠️ <b>Risk:</b> You may believe automation is active when it isn't, or vice versa — both are dangerous.</div>"
                    "</div>"

                    "</div><br>"
                    "Which of these three traps do you think would be hardest for you to avoid?"
                ),
                "yes_followup": "Interesting! All three are common — Let's address each one.",
                "no_followup": (
                    "Let me give a concrete example of each:\n\n"
                    "Over-trust → Driver watches a full movie, misses urgent TOR.\n"
                    "Complacency → After 90-minute highway drive, driver is slow to respond — crash.\n"
                    "Mode confusion → Driver thinks automation is on, removes hands from wheel — it wasn't on.\n\n"
                    "Each trap is different, but all three lead to the same problem: "
                    "not being ready when the system needs you. Does that make the risks clearer?"
                ),
            },
            {
                "message": (
                    "Here's how to stay alert and avoid all three traps:\n\n"
                    "<div style='display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:8px 0;'>"

                    # 1
                    "<div style='background:#eff6ff; border:1px solid #bfdbfe; border-radius:10px; padding:14px;'>"
                    "<div style='font-size:28px; margin-bottom:6px;'>1️⃣</div>"
                    "<div style='font-weight:700; color:#1d4ed8; margin-bottom:4px;'>Scan the Road</div>"
                    "<div style='font-size:12px; color:#6b7280; font-weight:600; margin-bottom:6px;'>Every 30–60 seconds</div>"
                    "<div style='font-size:13px; color:#374151;'>Briefly glance up at the road. Keeps situational awareness active and reduces TOR response time.</div>"
                    "</div>"

                    # 2
                    "<div style='background:#eff6ff; border:1px solid #bfdbfe; border-radius:10px; padding:14px;'>"
                    "<div style='font-size:28px; margin-bottom:6px;'>2️⃣</div>"
                    "<div style='font-weight:700; color:#1d4ed8; margin-bottom:4px;'>Interruptible Tasks Only</div>"
                    "<div style='font-size:12px; color:#6b7280; font-weight:600; margin-bottom:6px;'>Stop within seconds</div>"
                    "<div style='font-size:13px; color:#374151;'>Phone calls, audio, light reading ✅<br>Movies, games, deep focus ❌</div>"
                    "</div>"

                    # 3
                    "<div style='background:#eff6ff; border:1px solid #bfdbfe; border-radius:10px; padding:14px;'>"
                    "<div style='font-size:28px; margin-bottom:6px;'>3️⃣</div>"
                    "<div style='font-weight:700; color:#1d4ed8; margin-bottom:4px;'>Verify HMI First</div>"
                    "<div style='font-size:12px; color:#6b7280; font-weight:600; margin-bottom:6px;'>At every transition</div>"
                    "<div style='font-size:13px; color:#374151;'>Before looking away — glance at the dashboard. Confirm the mode. Then act.</div>"
                    "</div>"

                    # 4
                    "<div style='background:#eff6ff; border:1px solid #bfdbfe; border-radius:10px; padding:14px;'>"
                    "<div style='font-size:28px; margin-bottom:6px;'>4️⃣</div>"
                    "<div style='font-weight:700; color:#1d4ed8; margin-bottom:4px;'>Be Honest About Your Condition</div>"
                    "<div style='font-size:12px; color:#6b7280; font-weight:600; margin-bottom:6px;'>Know your limits</div>"
                    "<div style='font-size:13px; color:#374151;'>Tired, stressed, or medicated? Reconsider using Level 3. If you can't take over — don't rely on automation.</div>"
                    "</div>"

                    "Does this set of staying-alert strategies make sense?"
                ),
                "yes_followup": "Good. Let's wrap up with the <b>Three Golden Rules.</b>",
                "no_followup": (
                    "The core idea is: don't let automation make you a passive passenger.\n\n"
                    "Stay connected to the drive — just at a lower level of effort.\n"
                    "A quick glance at the road, a check of the HMI, and an honest assessment of how you're feeling "
                    "are all it takes to stay safe. Does that framing help?"
                ),
            },
            {
                "message": (
                    "To close out your training — Three Golden Rules:\n\n"
                    "<div style='display:flex; flex-direction:column; gap:10px; margin:8px 0;'>"

                    # Rule 1 - Blue
                    "<div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:4px solid #1d4ed8; border-radius:10px; padding:14px; display:flex; align-items:flex-start; gap:12px;'>"
                    "<div style='font-size:32px; flex-shrink:0;'>🤝</div>"
                    "<div>"
                    "<div style='font-weight:700; color:#1d4ed8; font-size:15px; margin-bottom:4px;'>Rule 1 — Responsible Partner, Not a Passenger</div>"
                    "<div style='font-size:13px; color:#374151;'>Level 3 is conditional automation. You share responsibility and must be ready to take over at any moment.</div>"
                    "</div>"
                    "</div>"

                    # Rule 2 - Green
                    "<div style='background:#f0fdf4; border:1px solid #86efac; border-left:4px solid #22c55e; border-radius:10px; padding:14px; display:flex; align-items:flex-start; gap:12px;'>"
                    "<div style='font-size:32px; flex-shrink:0;'>👁️</div>"
                    "<div>"
                    "<div style='font-weight:700; color:#15803d; font-size:15px; margin-bottom:4px;'>Rule 2 — Stay in the Loop</div>"
                    "<div style='font-size:13px; color:#374151;'>Periodic road scans keep your response time sharp and prevent out-of-loop performance degradation.</div>"
                    "</div>"
                    "</div>"

                    # Rule 3 - Red
                    "<div style='background:#fef2f2; border:1px solid #fca5a5; border-left:4px solid #ef4444; border-radius:10px; padding:14px; display:flex; align-items:flex-start; gap:12px;'>"
                    "<div style='font-size:32px; flex-shrink:0;'>❓</div>"
                    "<div>"
                    "<div style='font-weight:700; color:#dc2626; font-size:15px; margin-bottom:4px;'>Rule 3 — When in Doubt, Drive Manually</div>"
                    "<div style='font-size:13px; color:#374151;'>Uncertain about the weather, your condition, or the system? Take manual control. It is <b>always</b> the safest choice.</div>"
                    "</div>"
                    "</div>"

                    "</div><br>"
                    "That completes your <b>Level 3 Automation training!</b> 🎉 <br><br>"
                    "You're now ready for the final quiz. Does everything we covered make sense?"
                ),
                "yes_followup": (
                    "Fantastic! Let's move on to the post-training quiz. "
                    "This is your chance to show what you've learned. Good luck! 🍀"
                ),
                "no_followup": (
                    "Here's the entire training in three sentences:\n\n"
                    "Level 3 drives for you — but only under specific conditions.\n"
                    "When it reaches its limits, it asks you to take over — and you must respond promptly.\n"
                    "Stay alert, stay honest about your condition, and when in doubt, drive manually.\n\n"
                    "That's the foundation of safe Level 3 driving. Ready for the quiz?"
                ),
            },
        ],
    },
]


# =============================================================================
# TRAINING TOPICS — Group 4 ONLY (AI-generated conversation)
# Two content versions: Group A (Foundation) and Group B (Advanced)
# The AI instructor uses this as the knowledge base for conversation.
# =============================================================================

TRAINING_TOPICS = [
    {
        "title": "Module 1: Core Concepts of Level 3 Automation",
        "content_group_a": """
SAE Level 3 — Conditional Automation. Teach in plain, conversational language.

Key points to cover:
- SAE levels 0–5 overview: brief, simple, non-technical
- Level 3 definition: system drives and monitors, driver does NOT need to watch constantly,
  but MUST respond to Takeover Requests (TOR)
- Level 2 vs Level 3: key difference is WHO monitors the road (driver at L2, system at L3)
- Driver responsibilities: stay in seat, stay capable, respond to every TOR, check dashboard
- What NOT to do: sleep, leave seat, ignore TOR, drive impaired, do uninterruptible tasks
- Dashboard states: Green (active), Yellow (prepare), Red (act NOW), Gray (manual only)

Tone: Simple analogies, everyday language, encourage questions. Avoid jargon.
Real-world example: Mercedes-Benz DRIVE PILOT as first approved Level 3 system.
        """,
        "content_group_b": """
SAE Level 3 — Conditional Automation. Use technical depth appropriate for experienced drivers.

Key points to cover:
- SAE J3016 standard: DDT (Dynamic Driving Task), ODD, TOR definitions
- Level 3 distinction: system assumes full DDT responsibility within ODD;
  liability shifts to manufacturer during automated operation
- Level 2 vs Level 3: supervisory role vs fallback-ready role
- Driver responsibilities in detail: physical readiness, TOR compliance, HMI monitoring protocol
- Behavioral risks: automation bias, complacency, mode confusion
- Dashboard HMI: color-coded states and what each requires from the driver

Tone: Technically accurate, can reference research concepts, treat participant as knowledgeable.
Reference: SAE J3016, Mercedes DRIVE PILOT approval in Germany (2021) and Nevada (2023).
        """,
    },
    {
        "title": "Module 2: Operational Design Domains (ODD)",
        "content_group_a": """
Explain ODD in simple, practical terms.

Key points to cover:
- ODD = the specific conditions where Level 3 is designed to work safely
- Defined by the manufacturer — not the driver's choice
- Four ODD categories (all must be met simultaneously):
  1. Road type: highways and limited-access roads YES; city streets, roundabouts, construction NO
  2. Traffic: moderate predictable flow YES; dense chaotic traffic, cyclists/pedestrians increase risk
  3. Environment: clear weather and daylight YES; heavy rain, fog, snow, ice NO
  4. Geography: pre-mapped roads with GPS YES; tunnels, unmapped roads, unsupported regions NO
- Practical tip: check route before activating (tunnels, construction, weather forecast)

Tone: Use concrete examples ("imagine you're on I-95 vs. a downtown intersection").
Avoid technical sensor terminology. Focus on practical decision-making.
        """,
        "content_group_b": """
Explain ODD with technical and regulatory depth.

Key points to cover:
- ODD definition per SAE J3016: the specific operating domain within which
  the ADS is designed to function (road type, speed, environment, geography)
- Four ODD categories and simultaneous requirement
- Sensor dependencies: LiDAR, camera, radar — degradation modes for each condition
- Road type: structured environments; failure examples with technical explanation
- Traffic: cut-in detection limits, vulnerable road user (VRU) classification issues
- Environment: sensor physics — why fog degrades all sensors, why ice causes ODD exit
- Geography: HD map requirements, GPS multi-path error, centimeter-level localization
- System boundary vs. capability distinction: ODD is not a capability ceiling

Tone: Technical depth welcome. Can reference sensor physics and regulatory frameworks.
        """,
    },
    {
        "title": "Module 3: Takeover Requests (TOR)",
        "content_group_a": """
Explain TOR simply and practically.

Key points to cover:
- TOR = the car's way of saying "I need you to take over now"
- Alert types: visual (dashboard flash), audible (escalating tones), haptic (seat/wheel vibration)
- Three TOR types:
  1. Planned (25-30 sec): route boundary approaching — wrap up and take over smoothly
  2. Urgent (4-7 sec): unexpected event — drop everything, hands on wheel immediately
  3. Failure: system stops car (MRC) — help if possible, steer to shoulder
- 6-step response: Eyes on road → Hands on wheel → Stabilize lane → Assess →
  Apply brake/accelerate → Confirm manual control
- Key rule: always respond to every TOR, no exceptions

Tone: Use urgency appropriately. Concrete step-by-step. Relatable analogies.
        """,
        "content_group_b": """
Explain TOR with human factors and technical depth.

Key points to cover:
- TOR taxonomy: planned vs. urgent vs. failure; timing budgets for each
- Alert modalities: visual, audible, haptic — escalation design rationale
- Out-of-the-Loop (OOTL) phenomenon: how automation reduces situational awareness over time;
  response time degradation after 60+ min automation (2-3x slower)
- 6-step TOR execution protocol with biomechanical rationale
- Minimal Risk Condition (MRC): system behavior during failure TOR
- Human factors in TOR performance: secondary task engagement, vigilance decrement
- Research finding: drowsy drivers take 8+ sec vs. 3 sec for alert drivers

Tone: Reference human factors research where appropriate. Expect participant to engage critically.
        """,
    },
    {
        "title": "Module 4: HMI Dashboard Signals",
        "content_group_a": """
Explain HMI dashboard states in practical, easy-to-remember terms.

Key points to cover:
- HMI (Human-Machine Interface) = your window into what the automation is doing
- Four states:
  Green = system active, you can do permitted tasks
  Yellow = prepare to take over, wrap up tasks, get ready
  Red = take over NOW, act within seconds
  Gray = system unavailable, drive manually
- Key habit: verify HMI BEFORE looking away from the road
- Glance at dashboard every 30–60 seconds to stay aware
- Mode confusion prevention: always confirm Green before engaging non-driving tasks

Tone: Simple, memorable. Use traffic light analogy if helpful.
        """,
        "content_group_b": """
Explain HMI with design rationale and behavioral implications.

Key points to cover:
- HMI role in Level 3: primary mode awareness channel; driver's interface to DDT handover
- Four state system: Green (active), Yellow (transition warning), Red (urgent TOR), Gray (fault)
- Design rationale: color-coding for rapid recognition; escalating urgency in alerts
- Mode confusion as behavioral risk: false sense of automation engagement
- Verification protocol: HMI check before every non-driving task engagement
- Research context: mode confusion implicated in multiple real-world ADS incidents
- 30-60 second glance protocol: maintains situational awareness without continuous monitoring burden

Tone: Can discuss interface design principles and human factors behind HMI design.
        """,
    },
    {
        "title": "Module 5: Driver Issues — Overtrust, Complacency, Mode Confusion",
        "content_group_a": """
Help participants recognize and avoid the three behavioral traps.

Key points to cover:
- Most Level 3 incidents are caused by driver behavior, not system failure
- Three traps:
  1. Over-trust: "the car handles everything" → miss TOR, not ready
  2. Complacency: "nothing has gone wrong, so it won't" → response times degrade after 60+ min
  3. Mode confusion: "is it in auto right now?" → dangerous misunderstanding of current state
- Staying alert strategies:
  1. Scan road every 30-60 seconds
  2. Choose interruptible tasks only
  3. Verify HMI before looking away
  4. Be honest about your physical condition
- Three Golden Rules: responsible partner, stay in the loop, when in doubt drive manually

Tone: Empathetic and practical. Normalize that these traps happen to everyone.
        """,
        "content_group_b": """
Cover behavioral risks with research context and depth.

Key points to cover:
- Automation complacency literature: Parasuraman & Riley (1997) automation bias framework
- Out-of-the-Loop (OOTL): vigilance decrement over extended automation; 2-3x TOR response time increase
- Mode confusion: cognitive basis, real-world examples in aviation and automotive ADS
- Over-trust / automation bias: commission errors vs. omission errors
- Appropriate trust calibration: mental model accuracy as predictor of TOR performance
- Countermeasures: road scanning protocol, task interruptibility framework, HMI verification habit
- Three Golden Rules in context: shared responsibility model, vigilance maintenance, conservative override
- Forward-looking: as Level 3 becomes more common, training and calibrated trust become critical safety factors

Tone: Engage participant as a critical thinker. Reference research. Expect substantive discussion.
        """,
    },
]


# =============================================================================
# QUIZ QUESTIONS — Same for ALL groups (3 & 4) and knowledge groups (A & B)
# Administered AFTER all training modules are complete.
# =============================================================================

QUIZ_QUESTIONS = [
    {
        "q": "What does SAE Level 3 automation require of the driver?",
        "options": {
            "A": "The driver can sleep as the system handles everything",
            "B": "The driver must keep hands on the wheel at all times",
            "C": "The driver must be ready to take over when the system requests it",
            "D": "The driver must monitor the road continuously without looking away"
        },
        "answer": "C",
        "explanation": (
            "Level 3 allows the driver to disengage from monitoring, but they must respond "
            "promptly to a Takeover Request (TOR). Sleeping or refusing to respond is unsafe and prohibited."
        )
    },
    {
        "q": "Which of the following is within the typical Operational Design Domain (ODD) of a Level 3 system?",
        "options": {
            "A": "Urban intersection during rush hour",
            "B": "Highway driving at moderate speed in clear weather on a pre-mapped road",
            "C": "Snowy mountain roads at night",
            "D": "A school zone with pedestrians present"
        },
        "answer": "B",
        "explanation": (
            "Level 3 systems are designed for structured, predictable environments like mapped highways "
            "in good weather. City intersections, snow, and school zones are outside ODD."
        )
    },
    {
        "q": "Which of the following should a driver NOT do while Level 3 automation is active?",
        "options": {
            "A": "Listen to a podcast",
            "B": "Have a phone conversation",
            "C": "Watch a full-length movie",
            "D": "Check messages briefly"
        },
        "answer": "C",
        "explanation": (
            "Activities that cannot be stopped within a few seconds are prohibited. "
            "Watching a movie causes deep focus that prevents timely TOR response. "
            "Audio tasks (podcasts, calls) can be paused immediately."
        )
    },
    {
        "q": "What does a RED dashboard warning signal mean in a Level 3 vehicle?",
        "options": {
            "A": "The system is fully active — you may look away",
            "B": "A Takeover Request is approaching — begin wrapping up tasks",
            "C": "Take over manual control immediately",
            "D": "The system has a minor fault but can continue"
        },
        "answer": "C",
        "explanation": (
            "Red means urgent TOR — act within seconds. "
            "Green = active, Yellow = prepare, Red = act NOW, Gray = manual only."
        )
    },
    {
        "q": "What is the FIRST step to take when a Takeover Request (TOR) is issued?",
        "options": {
            "A": "Apply the brake immediately",
            "B": "Check mirrors and blind spots",
            "C": "Look up and assess the road ahead",
            "D": "Turn off the automation system"
        },
        "answer": "C",
        "explanation": (
            "Eyes to road is step 1. You need situational awareness before any physical action. "
            "Hands on wheel is step 2, lane stabilization is step 3."
        )
    },
    {
        "q": "Which type of Takeover Request gives the driver the least response time?",
        "options": {
            "A": "Planned TOR",
            "B": "Urgent TOR",
            "C": "Failure TOR",
            "D": "Scheduled TOR"
        },
        "answer": "C",
        "explanation": (
            "Failure TOR is a critical system fault with no defined warning window — "
            "the vehicle initiates Minimal Risk Condition automatically. "
            "Planned TOR gives 25-30 seconds; Urgent TOR gives 4-7 seconds."
        )
    },
    {
        "q": "What behavioral trap describes a driver who thinks 'nothing has gone wrong for weeks, so it won't today'?",
        "options": {
            "A": "Over-trust",
            "B": "Mode confusion",
            "C": "Complacency",
            "D": "Under-trust"
        },
        "answer": "C",
        "explanation": (
            "Complacency (Out-of-the-Loop) is the false sense of security from extended trouble-free automation. "
            "Research shows TOR response times can be 2-3x slower after 60+ minutes of automation."
        )
    },
    {
        "q": "Which of the following conditions is OUTSIDE the ODD of a typical Level 3 system?",
        "options": {
            "A": "Clear highway with visible lane markings",
            "B": "Light rain on a pre-mapped motorway",
            "C": "Dense fog on any road type",
            "D": "Nighttime driving on a well-lit highway"
        },
        "answer": "C",
        "explanation": (
            "Dense fog degrades all sensors (camera, LiDAR, radar) and causes immediate ODD exit. "
            "Light rain, well-lit night roads, and clear highways are generally within ODD."
        )
    },
]


# =============================================================================
# STRUCTURED FEEDBACK — Group 3 ONLY
# Pre-written, identical for all Group 3 participants.
# Two versions: Knowledge Group A and Knowledge Group B.
# Does NOT reference individual quiz answers.
# =============================================================================

STRUCTURED_FEEDBACK_GROUP_A = (
    "Thank you for completing the Level 3 Automation Driver Training. Well Done!"
)

STRUCTURED_FEEDBACK_GROUP_B = (
    "Thank you for completing the Level 3 Automation Driver Training. Well Done! "
)


# =============================================================================
# CHATBOT SYSTEM PROMPT — Group 4 ONLY
# Governs AI instructor behavior across all topics and knowledge groups.
# =============================================================================

CHATBOT_SYSTEM_PROMPT = """
You are an expert AI instructor delivering Level 3 automated driving training
to participants in a research study. You teach based on SAE J3016 standards
and established human factors research.

Your role:
- Lead the conversation — introduce each topic, explain clearly, then invite discussion
- Adapt depth to Knowledge Group: A = Foundation (plain language, analogies),
  B = Advanced (technical accuracy, research references)
- Keep responses concise: 3–6 sentences, then ask one follow-up question
- Stay strictly on-topic: Level 3 automation, ODD, TOR, HMI, driver behavior
- Be warm, encouraging, and never condescending
- Do NOT reveal you are following a content script

If asked something outside scope:
"Good question! For this session, let's stay focused on Level 3 automation —
we can explore that further after the training."

Key content to draw from across all modules:
- SAE Levels 0-5; Level 3 = Conditional Automation
- ODD: Road type, Traffic, Environment, Geography — all four must be met
- Driver responsibilities: stay in seat, respond to every TOR, check HMI, stay capable
- Prohibited behaviors: sleeping, leaving seat, ignoring TOR, impaired driving, uninterruptible tasks
- HMI: Green/Yellow/Red/Gray states and appropriate driver actions
- TOR types: Planned (25-30s), Urgent (4-7s), Failure (MRC)
- TOR response: Eyes → Hands → Stabilize → Assess → Speed → Confirm
- Behavioral traps: Over-trust, Complacency (OOTL), Mode Confusion
- Countermeasures: road scans, interruptible tasks, HMI verification, honest self-assessment
- Three Golden Rules: responsible partner, stay in loop, manual when in doubt
"""
