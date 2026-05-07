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
                    "Welcome to your <b>Level 3 Automation Driver Training!</b> 🚗 <br><br>"
                    "Let's start with a quick overview of SAE automation levels. "
                    "Take a look at the diagram below — it shows all six levels defined by SAE International J3016:<br><br>"
                    "<b>Level 0 — No Automation: </b>"
                    "Full and constant responsibility for all dynamic driving tasks. No system support. The driver is the human operator. <br><br>"
                    "<b>Level 1 — Driver Assistance: </b>\n"
                    "The vehicle features a single automated system (e.g. speed or steering control). "
                    "Driver must monitor and adjust continuously. Supervised control.<br><br>"
                    "<b>Level 2 — Partial Automation: </b>\n"
                    "The vehicle can perform steering and acceleration. "
                    "Driver must monitor continuously and take control at any time. Combined monitoring.<br><br>"
                    "<b>Level 3 — Conditional Automation: </b> (<b>Today's focus</b>)\n"
                    "The vehicle can perform most driving tasks under specific conditions. "
                    "Driver is NOT responsible for monitoring, but MUST be ready to take over on request. Fallback ready.<br><br>"
                    "<b>Level 4 — High Automation: </b>\n"
                    "The vehicle handles all driving tasks under most conditions autonomously. "
                    "Minimal intervention might be necessary. Limited use.<br><br>"
                    "<b>Level 5 — Full Automation:</b>\n"
                    "The vehicle handles all driving tasks under all conditions autonomously. "
                    "No driver responsibility for any aspect of the dynamic driving task. No driver required.<br><br>"
                    "Does this overview of SAE levels make sense to you? Click the image to enlarge."
                ),
                "image": "Sae levels.png",
                "yes_followup": "Great! Let's look at what Level 3 specifically means for you as a driver.",
                "no_followup": (
                    "No problem! Here's the key difference to focus on: <br><br>"
                    "At <b>Level 2</b>, The human driver is still the primary driver at all times. The system can assist with steering and speed control, but the driver must continuously monitor the environment and be ready to intervene immediately.<br><br> → <i>You are driving, and the system is assisting you</i>. <br><br>"
                    "At <b>Level 3</b>, The automated system becomes the primary driver under specific conditions. The human driver does not need to continuously monitor the environment, but must be ready to take over when the system requests it.<br><br> → <i>The system is driving, and you engage only when needed</i>. <br><br>"
                    "Think of it as: <b>Level 2</b> = human driver <b>needs</b> to continuously monitor the surroundings, <b>Level 3</b> = human driver <b>doesn't need</b> to continuously monitor the surroundings, unless necessary.<br><br>"
                    "Does that help clarify the difference?"
                ),
            },
            {
                "message": (
                    "So what exactly is <b>Level 3 — Conditional Automation</b>?<br><br>"
                    "🤖 <b>The system takes the control:</b> <br><br>"
                    "The vehicle <b>steers, accelerates, and brakes</b> on its own. "
                    "The system monitors the environment.<br><br>"
                    "⚠️ <b>Conditional, not full automation:</b> <br><br>"
                    "It only works within a <b>specific Operational Design Domain (ODD)</b> — "
                    "defined road types, speed ranges, and weather conditions set by the manufacturer.<br><br>"
                    "🔄 <b>Takeover is your responsibility</b>:<br><br>"
                    "When the system <b>reaches its limits</b>, it issues a <b>Takeover Request (ToR)</b>. "
                    "You <b>MUST</b> respond promptly.<br><br>"
                    "Does this definition of Level 3 make sense to you?"
                ),
                "yes_followup": None,
                "no_followup": (
                    "Let's simplify to three rules:<br><br>"
                    "1. The automated driving systems drives the car automatically — <b>but only under specific conditions</b>.<br><br>"
                    "2. You don't need to monitor the road, but need to stay available to take over.<br><br>"
                    "3. When the systems asks for manual takeover → <b>Take over immediately</b>.<br><br>"
                    "That's the core of Level 3. Ready to continue?"
                ),
            },
            {
                "message": (
                    "<b>A key distinction: Level 2 vs. Level 3.</b><br><br>"
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
                    "<td style='padding:10px; font-weight:600;'>Takeover Request (ToR)?</td>"
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
                    "Here's the simplest way to remember it:<br><br>"
                    "<b>Level 2</b> = Hands-off, but EYES ON the road at all times.<br><br>"
                    "<b>Level 3</b> = Eyes can be off the road, but BE READY to take over.<br><br>"
                    "That one difference is what makes Level 3 a significant step forward — "
                    "and why understanding your responsibilities matters so much. Clear now?"
                ),
            },
            {
                "message": (
                    "Here's what you <span style='color:#1d4ed8; font-weight:700;'>ARE</span> responsible for during Level 3 automation:<br><br>"
                    "💺 <b>Stay in the driver's seat at all times</b> — You must remain in the driver's seat and within reach of the steering wheel at all times.<br><br>"
                    "🚨 <b>Be physically able to resume control and stay alert</b> — Do not drive tired, impaired, or medicated.<br><br>"
                    "🖐️ <b>Hands and feet ready when alerted</b> — When a Takeover Request is issued, place hands on the wheel and feet near the pedals.<br><br>"
                    "⚡ <b>Respond to every Takeover Request</b> — You must take over when the system alerts you for either planned or urgent. Never dismiss or delay.<br><br>"
                    "📊 <b>Monitor the dashboard every 30–60 seconds</b> <br><br>"
                    "Does this list of driver responsibilities make sense?"
                ),
                "yes_followup": "Good. Now let's look at what you should <b>NOT</b> do during Level 3.",
                "no_followup": (
                    "Think of it this way — Level 3 reduces your workload, but does <b>NOT</b> eliminate your role.<br><br>"
                    "You still need to:<br><br>"
                    "• Stay in the seat<br><br>"
                    "• Stay awake and capable<br><br>"
                    "• Respond to alerts<br><br>"
                    "• Glance at the dashboard occasionally<br><br>"
                    "The system drives. You remain the responsible backup. Does that make sense?"
                ),
            },
            {
                "message": (
                    "And here's what you should <span style='color:#ef4444; font-weight:700;'>NOT</span> do while Level 3 automation is active:<br><br>"
                    "😴 <b>Sleep or become fully unresponsive</b> — Drowsy drivers need more response time to react compared to drivers who are alert.<br><br>"
                    "💺 <b>Leave the driver's seat</b> — You must remain within reach of the steering wheel at all times during automation..<br><br>"
                    "❗️ <b>Ignore or dismiss a ToR alert</b> — You must takeover if you receive a ToR request.<br><br>"
                    "🍺 <b>Drive under the influence</b> — Alcohol, drugs, or impairing medication are prohibited regardless of automation level.<br><br>"
                    "⏳ <b>Engage in tasks you can't stop immediately</b> — Only do things you can interrupt within seconds.<br><br>"
                    "Does this list of prohibited behaviors make sense?"
                ),
                "yes_followup": (
                    "Great! You've completed <b>Module 1</b>. 🎉<br><br>"
                    "Let's move on to <b>Module 2: Operational Design Domains</b> — "
                    "the specific conditions under which Level 3 can and cannot operate."
                ),
                "no_followup": (
                    "The key rule is: only do things you can <b>STOP</b> within a few seconds.<br><br>"
                    "<b>Phone call?</b> OK — you can put it down.<br><br>"
                    "<b>Watching a movie?</b> Not OK — you'll be too absorbed.<br><br>"
                    "<b>Napping?</b> Definitely not — you won't hear the ToR alert.<br><br>"
                    "Level 3 gives you a break from driving, not from being a driver. Ready to continue?"
                ),
            },
        ],
    },

    # ── MODULE 2: Operational Design Domain ──────────────────────────────────
    {
        "title": "Module 2: Operational Design Domains (ODD) <br><br>",
        "steps": [
            {
                "message": (
                    "<b>Module 2: Operational Design Domains (ODD)</b><br><br>"
                    "The <b>ODD</b> defines the <b>specific environmental, roadway, and traffic conditions</b> under which a Level 3 automated driving system is designed to perform the driving task safely. <br><br>"
                    "<ul style='margin:8px 0; padding-left:20px;'>"
                    "🗂️ <b>System Boundary</b> <br><br>"
                    "<span style='color:#ef4444; font-weight:700;'>Important points:</span>"
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
                    "💡 ODD does not mean the system is perfect within those conditions. Real-world conditions can still vary. Safe use starts with understanding this distinction.<br><br>"
                    "<b>Does the concept of ODD make sense?</b>"
                ),

                "yes_followup": "Good. Let's look at the four ODD condition categories.",
                "no_followup": (
                    "Think of <b>ODD</b> like the operating manual for an appliance:<br><br>"
                    "A washing machine is designed for clothes — not bricks. "
                    "It might handle one brick, but it's not built for it and could break.<br><br>"
                    "Similarly, Level 3 is designed for specific road conditions. "
                    "Outside those, it can't guarantee safe operation.<br><br>"
                    "The manufacturer defines exactly what those conditions are. Does that explanation help?"
                ),
            },
            {
                "message": (
                    "ODD is defined by <b>four condition</b> categories — ALL must be met simultaneously:<br><br>"
                    "🛣️ <b>01. Road Type & Geometry</b> <br><br>"
                    "🚗 <b>02. Traffic Conditions</b> <br><br>"
                    "🌤️ <b>03. Environmental Conditions</b> <br><br>"
                    "🗺️ <b>04. Geographic Area & Map</b> <br><br>"
                    
                    "⚠️ <b>All Four conditions must be satisfied simultaneously.</b> <br><br> <b>Failure of even one category</b> can cause the system to issue a Takeover Request — even if all other conditions are fine.<br><br>"
                    "Does this <b>four condition categories</b> make sense?"
                ),
                "yes_followup": "Good. Let's go through each category in more detail.",
                "no_followup": (
                    "Think of it like a checklist before activation:<br><br>"
                    "✅ Road type OK?<br><br>"
                    "✅ Traffic OK?<br><br>"
                    "✅ Weather OK?<br><br>"
                    "✅ GPS & map OK?<br><br>"
                    "If even one item on that checklist fails, the system may exit automation. "
                    "All four conditions should be met at the same time. Does that make it clearer?"
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
                    "<li>Construction zones</li>"
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
                    "<li>Dense or heavy traffic</li>"
                    "<li>Cyclists &amp; pedestrians</li>"
                    "<li>Emergency vehicles nearby</li>"
                    "</ul></td>"
                    "</tr>"
                    "</tbody>"
                    "</table>"
                    "<br>💡 <b>Roadway condition</b> is the most common reason Level 3 disengages — always check your route before activating.<br>"
                    "💡 Even within ODD, high <b>traffic complexity</b> can trigger an urgent TOR — stay alert in dense traffic.<br><br>"
                    "Is this clear so far?"
                ),
                "yes_followup": "Good. Let's look at <b>environmental and geographic conditions.</b>",
                "no_followup": (
                    "Here's the simple version:<br><br>"
                    "Roadway → Highways YES, city streets NO.<br><br>"
                    "Traffic → Predictable flow YES, heavy or unpredictable NO.<br><br>"
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
                    "<li>High-level GPS available</li>"
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
                    "Here's the short version for <b>environmental and geographic conditions</b>:<br><br>"
                    "Environment → Good visibility and weather YES, fog/snow/ice NO.<br><br>"
                    "Geography → Mapped highways with GPS YES, tunnels/unmapped roads/unsupported regions NO.<br><br>"
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
                    "<b>Module 3: Takeover Requests (ToR)</b>🚨<br><br>"
                    "<b>A Takeover Request (ToR)</b> is the system's signal: "
                    "\"<b>I cannot continue safely — please take manual control now.</b>\"<br><br>"
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
                    "Does this concept makes you clear?"
                ),
                "yes_followup": "Good. Lets move on to how to correctly takeover in sequece.",
                "no_followup": (
                    "Think of a TㅐR like a system handover request: The system is telling you, 'I’ve reached my limit — you need to take control now.'<br><br>"
                    "It does not always mean there is immediate danger, but it means the system can no longer reliably handle the situation.<br><br>"
                    "Your job is simply to respond promptly and take control. "
                    "We'll walk through exactly how to do that next. Ready?"
                ),
            },
            {
                "message": (
                    "When a TOR is issued, execute these 5 steps in order:\n\n"
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
                    "<div><div style='font-weight:700; color:#1d4ed8;'>Assess Surroundings and Stabilize Lane</div>"
                    "<div style='font-size:13px; color:#374151;'>Check mirrors, blind spots, and what triggered the ToR. Maintain your lane position smoothly. No sudden steering.</div></div>"
                    "</div>"

                    "<div style='display:flex; align-items:flex-start; gap:12px; background:#f8f9fb; border:1px solid #e5e7eb; border-radius:10px; padding:12px;'>"
                    "<div style='background:#1d4ed8; color:white; border-radius:50%; width:28px; height:28px; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:13px; flex-shrink:0;'>4</div>"
                    "<div><div style='font-weight:700; color:#1d4ed8;'>Apply Brake / Acceleration</div>"
                    "<div style='font-size:13px; color:#374151;'>React to the road situation and adjust speed as needed.</div></div>"
                    "</div>"

                    "<div style='display:flex; align-items:flex-start; gap:12px; background:#f8f9fb; border:1px solid #e5e7eb; border-radius:10px; padding:12px;'>"
                    "<div style='background:#1d4ed8; color:white; border-radius:50%; width:28px; height:28px; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:13px; flex-shrink:0;'>5</div>"
                    "<div><div style='font-weight:700; color:#1d4ed8;'>Confirm Full Manual Control</div>"
                    "<div style='font-size:13px; color:#374151;'>Verify automation is OFF on the HMI. You are now in control.</div></div>"
                    "</div>"

                    "</div><br>"
                    "Does this <b>5-step ToR response process</b> make sense?"
                ),
                "yes_followup": "Good. Now let's look at the three different types of ToR.",
                "no_followup": (
                    "Let's simplify to the first three steps — the most critical ones:<br><br>"
                    "Step 1: Look at the road.<br><br>"
                    "Step 2: Grab the wheel.<br><br>"
                    "Step 3: Don't swerve — stabilize first.<br><br>"
                    "Steps 4-5: follow naturally once you're in control. <br><br> "
                    "The key is: eyes and hands first, assessment second. Clear?"
                ),
            },
            {
                "message": (
                    "There are two types of ToR — each requires a different response speed:<br><br>"
                    "<div style='display:flex; flex-direction:column; gap:10px; margin:8px 0;'>"

                    # Planned TOR - Green
                    "<div style='background:#f0fdf4; border:1px solid #86efac; border-left:4px solid #22c55e; border-radius:10px; padding:14px;'>"
                    "<div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;'>"
                    "<div style='font-weight:700; color:#15803d; font-size:15px;'>1️⃣ PLANNED/Scheduled ToR</div>"
                    "<div style='background:#22c55e; color:white; border-radius:99px; padding:2px 10px; font-size:12px; font-weight:600;'>25–30 sec</div>"
                    "</div>"
                    "<div style='font-size:13px; color:#374151; margin-bottom:8px;'>System detects an upcoming ODD boundary (e.g., highway exit, construction ahead). Most situations are manageable within certain time.</div>"
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
 

                    "</div><br>"
                    "Does understanding the <b>two types of ToR</b> make sense?"
                ),
                "yes_followup": (
                    "Great! You've completed <b>Module 3</b>. 🎉<br><br>"
                    "<b>Module 4</b> covers <b>How the System Works</b> — specifically, the dashboard signals "
                    "that tell you what mode the system is in."
                ),
                "no_followup": (
                    "Here's the key takeaway for each type:<br><br>"
                    "<b>Planned ToR</b> → You have time. Wrap up and take over smoothly.<br><br>"
                    "<b>Urgent ToR</b> → No time. Drop everything and react immediately.<br><br>"
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
                    "There are dashboard HMI indicators you need to know:<br><br>"

                    "<div style='display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:8px 0;'>"

                    # GREEN
                    "<div style='background:#f0fdf4; border:2px solid #22c55e; border-radius:10px; padding:14px; text-align:center;'>"
                    f"<img src='data:image/png;base64,{green_img}' style='width:100%; border-radius:6px; margin-bottom:8px;'>"
                    "<div style='font-weight:700; color:#15803d; font-size:15px; margin-bottom:4px;'>🟢 GREEN — System Active</div>"
                    "<div style='font-size:13px; color:#374151;'>Automation fully engaged. You may engage in permitted non-driving tasks.</div>"
                    "</div>"


                    # RED
                    "<div style='background:#fef2f2; border:2px solid #ef4444; border-radius:10px; padding:14px; text-align:center;'>"
                    f"<img src='data:image/png;base64,{red_img}' style='width:100%; border-radius:6px; margin-bottom:8px;'>"
                    "<div style='font-weight:700; color:#dc2626; font-size:15px; margin-bottom:4px;'>🔴 RED — Take Over NOW</div>"
                    "<div style='font-size:13px; color:#374151;'>Drop everything. Hands on wheel. Eyes on road. Act within seconds.</div>"
                    "</div>"


                    "</div><br>"
                    "Does the <b>color HMI system</b> make sense?"
                    ),
                "yes_followup": (
                    "Excellent! You've completed <b>Module 4</b>. 🎉<br><br>"
                    "One more module to go — <b>Module 5 covers Driver Issues.</b> "
                    
                ),
                "no_followup": (
                    "Think of it like a traffic light — but for your automation system:<br><br>"
                    "🟢 Green = Go. System is driving. You're fine.<br><br>"
                    "🔴 Red = Stop (everything else). Take over RIGHT NOW.<br><br>"

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
                    "not system failure. There are three behavioral risks to be aware of:<br><br>"

                    "<div style='display:flex; flex-direction:column; gap:10px; margin:8px 0;'>"

                    # Risk 1
                    "<div style='background:#fffbeb; border:1px solid #fcd34d; border-left:4px solid #f59e0b; border-radius:10px; padding:14px;'>"
                    "<div style='font-weight:700; color:#92400e; font-size:15px; margin-bottom:6px;'>😌 Risk 1 — Over-Trust </div>"
                    "<div style='font-style:italic; color:#78350f; background:#fef3c7; border-radius:6px; padding:8px; margin-bottom:8px; font-size:13px;'>"
                    "\"The system handles everything. I don't need to stay alert.\""
                    "</div>"
                    "<div style='font-size:13px; color:#374151;'>⚠️ <b>Risk:</b> When the system hits its limits, you won't be ready to take over in time.</div>"
                    "</div>"

                    # Risk 2
                    "<div style='background:#eff6ff; border:1px solid #bfdbfe; border-left:4px solid #1d4ed8; border-radius:10px; padding:14px;'>"
                    "<div style='font-weight:700; color:#1d4ed8; font-size:15px; margin-bottom:6px;'>😶 Risk 2 — Unresponsiveness </div>"
                    "<div style='font-style:italic; color:#1e40af; background:#dbeafe; border-radius:6px; padding:8px; margin-bottom:8px; font-size:13px;'>"
                    "\"I’ll respond in a moment — I don’t need to react immediately.\""
                    "</div>"
                    "<div style='font-size:13px; color:#374151;'>⚠️ <b>Risk:</b>Delayed or no response to a takeover request can lead to insufficient time to stabilize the vehicle and avoid hazards.</div>"
                    "</div>"

                    # Risk 3
                    "<div style='background:#f0fdf4; border:1px solid #fcd34d; border-left:4px solid #22c55e; border-radius:10px; padding:14px;'>"
                    "<div style='font-weight:700; color:#15803d; font-size:15px; margin-bottom:6px;'>😵 Risk 3 — Mode Confusion</div>"
                    "<div style='font-style:italic; color:#22c55e; background:#dcfce7; border-radius:6px; padding:8px; margin-bottom:8px; font-size:13px;'>"
                    "\"Wait — is the car in automation mode right now or not?\""
                    "</div>"
                    "<div style='font-size:13px; color:#374151;'>⚠️ <b>Risk:</b> You may believe automation is active when it isn't, or vice versa — both are dangerous.</div>"
                    "</div>"

                    "</div><br>"
                    "Did you undertand the potential driver issues?"
                ),
                "yes_followup": "Perfect! Now let's address each one in detail!",
                "no_followup": (
                    "Let me give a concrete example of each:<br><br>"
                    "Over-trust → Driver watches a full movie, misses urgent TOR.<br><br>"
                    "Unresponsiveness → The driver sleeps and don't respond in time — crash.<br><br>"
                    "Mode confusion → Driver thinks automation is on, removes hands from wheel — it wasn't on.<br><br>"
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

                    "Does this set of strategies make sense?"
                ),
                "yes_followup": "Good. Let's wrap up with the <b>Three Golden Rules.</b>",
                "no_followup": (
                    "The core idea is: <b>Don't let automation make you a passive passenger.</b> <br><br>"
                    "Stay connected to the drive — just at a lower level of effort.<br><br>"
                    "A quick glance at the road, a check of the HMI, and an honest assessment of how you're feeling "
                    "are all it takes to stay safe. Does that framing help?"
                ),
            },
            {
                "message": (
                    "To close out your training — Three Golden Rules:<br><br>"
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
        "q": "According to SAE(Society of Automotive Engineers), which statement best describes a Level 3 automated driving system?",
        "options": {
            "A": "The vehicle handles all driving tasks in all conditions with no driver needed",
            "B": "The driver must monitor the road at all times while the system assists",
            "C": "The system performs all driving tasks within its ODD, but the driver must respond to takeover requests",
            "D": "The system controls only steering while the driver controls speed"
        },
        "answer": "C",
        "explanation": (
            "Level 3 (Conditional Automation) means the system handles all Dynamic Driving Tasks within its ODD, "
            "but the driver must respond to a Takeover Request (TOR) when the system reaches its limits. "
            "The driver does not need to monitor continuously, but must remain available."
        ),
        "feedback_group_a": (
            "The correct answer is <b>C</b>. Level 3 means the car drives itself within certain conditions, "
            "but you must take over when it asks. Think of it like a co-pilot — the system handles the driving, "
            "but you are always the responsible backup. "
            "You should always remember: Level 3 is NOT fully self-driving. "
            "When a Takeover Request is issued, you must respond immediately."
        ),
        "feedback_group_b": (
            "The correct answer is <b>C</b>. Level 3 automation performs all driving tasks within its ODD, but the driver must respond to takeover requests when the system reaches its limits."
        ),
    },
    {
        "q": "What is the key difference between Level 2 and Level 3 automation?",
        "options": {
            "A": "Level 3 is faster than Level 2",
            "B": "At Level 2, the driver must continuously monitor the surroundings; at Level 3, the system monitors surroundings within its ODD",
            "C": "Level 2 requires a special license; Level 3 does not",
            "D": "Level 3 works in all weather conditions; Level 2 does not"
        },
        "answer": "B",
        "explanation": (
            "The critical distinction is who monitors the driving environment. "
            "At Level 2, the driver must supervise at all times (eyes on road). "
            "At Level 3, the system monitors within its ODD — the driver can look away but must be ready to respond to a TOR."
        ),
        "feedback_group_a": (
            "The correct answer is <b>B</b>. The biggest difference between Level 2 and Level 3 is simple: "
            "at Level 2, your eyes must stay on the road at all times, even if the car is steering. "
            "At Level 3, the car watches the road for you — but only in certain conditions. "
            "You should always remember: even at Level 3, you must be ready to take back control the moment the car asks."
        ),
        "feedback_group_b": (
            "The correct answer is <b>B</b>. The key difference is monitoring responsibility — Level 2 requires continuous driver monitoring, while Level 3 allows the system to monitor within its ODD."
        ),
    },
    {
        "q": "Which of the following scenarios is WITHIN the Operational Design Domain (ODD) of a typical Level 3 system?",
        "options": {
            "A": "A roundabout in a school zone during heavy rain",
            "B": "A highway with clear lane markings in clear weather",
            "C": "A rural unmapped road at night",
            "D": "A city intersection with pedestrians and cyclists"
        },
        "answer": "B",
        "explanation": (
            "Level 3 systems are designed for structured, predictable environments: "
            "highways with clear markings, moderate speed, good weather, and pre-mapped roads. "
            "Roundabouts, unmapped roads, and city intersections are outside ODD."
        ),
        "feedback_group_a": (
            "The correct answer is <b>B</b>. Level 3 works best on highways with clear, predictable conditions — "
            "open road, good weather, and visible lane markings. "
            "It does not work in complex situations like city intersections, roundabouts, or bad weather. "
            "You should always check your route and conditions before activating Level 3."
        ),
        "feedback_group_b": (
            "The correct answer is <b>B</b>. A highway with clear lane markings in clear weather meets all four ODD conditions. The other options violate one or more ODD boundaries."
        ),
    },
    {
        "q": "All four ODD conditions must be satisfied simultaneously. Which combination would cause a Level 3 system to disengage?",
        "options": {
            "A": "Clear weather + highway + moderate traffic + pre-mapped road",
            "B": "Light rain + highway + steady traffic + GPS available",
            "C": "Dense fog + highway + moderate traffic + pre-mapped road",
            "D": "Daylight + highway + low traffic + manufacturer-approved region"
        },
        "answer": "C",
        "explanation": (
            "Dense fog degrades all system detection sensors and causes immediate ODD exit — "
            "even if road type, traffic, and geography conditions are all met. "
            "All four ODD categories must be satisfied simultaneously."
        ),
        "feedback_group_a": (
            "The correct answer is <b>C</b>. Dense fog blocks the car's sensors so it cannot see the road safely. "
            "Even if everything else is fine — highway, light traffic, GPS working — one bad condition is enough to shut the system down. "
            "You should always remember: all four conditions must be met at the same time. "
            "If even one fails, Level 3 disengages and you must take over."
        ),
        "feedback_group_b": (
            "The correct answer is <b>C</b>. Dense fog breaks the environmental conditions requirement. All four ODD conditions must be satisfied simultaneously for Level 3 to remain active."
        ),
    },
    {
        "q": "A driver receives a Takeover Request (ToR) while browsing on their phone. Which of the following is NOT an appropriate immediate response?",
        "options": {
            "A": "Looking up to assess the road ahead",
            "B": "Taking control of the steering wheel",
            "C": "Preparing to adjust speed if needed",
            "D": "Delaying response because the system is still active"
        },
        "answer": "D",
        "explanation": (
            "Delaying your response to a Takeover Request is never appropriate. "
            "A ToR means the system has reached its operational limits and requires you to take control immediately. "
            "All other options — looking up, taking the wheel, adjusting speed — are correct immediate actions. "
            "Even if the system appears to still be functioning, you must act without hesitation."
        ),
        "feedback_group_a": (
            "The correct answer is <b>D</b>. Delaying your response is never acceptable when the car asks you to take over. "
            "A Takeover Request means the system has reached its limit — it needs YOU right now. "
            "Even if it looks like the car is still driving fine, you must respond immediately. "
            "You should always treat every Takeover Request as urgent, no matter what you are doing."
        ),
        "feedback_group_b": (
            "The correct answer is <b>D</b>. Delaying your response is not acceptable. All other actions (looking up, taking the wheel, preparing to adjust speed) are appropriate immediate responses."
        ),
    },
    {
        "q": "A vehicle is approaching an area with unclear lane markings. The system detects that condition will soon exceed its operational limits and issues a takeover request in advance. This is an example of:",
        "options": {
            "A": "Planned ToR",
            "B": "Urgent ToR",
            "C": "System Failure",
            "D": "Driver Distraction"
        },
        "answer": "A",
        "explanation": (
            "This is a Planned TOR because the system can anticipate that it is approaching conditions outside its Operational Design Domain (ODD), such as faded lane markings."
            "Since the situation is predictable, the system provides the driver with time to prepare for takeover."
        ),
        "feedback_group_a": (
            "The correct answer is <b>A</b> — this is a Planned Takeover Request. "
            "The system saw the problem coming and gave you advance warning, so you have time to get ready. "
            "This is the most manageable type of takeover — you can finish what you are doing, put your hands on the wheel, and take over calmly. "
            "You should always use this extra time wisely rather than waiting until the last second."
        ),
        "feedback_group_b": (
            "The correct answer is <b>A</b>. When the system anticipates exceeding its operational limits and issues a ToR in advance, this is a Planned ToR."
        ),
    },
    {
        "q": "What does a Red icon HMI dashboard signal indicate?",
        "options": {
            "A": "The system has failed and you must drive manually immediately",
            "B": "Automation is fully active — you may engage in non-driving tasks",
            "C": "The system approached an ODD boundary — take over",
            "D": "A minor sensor issue has been detected but automation continues normally"
        },
        "answer": "C",
        "explanation": (
            "Red = Take over warning. The system is still active but approached an ODD boundary. "
            "You should wrap up any non-driving tasks and engage in manual control. <br><br>"
            "Green = active, Red = take over."
        ),
        "feedback_group_a": (
            "The correct answer is <b>C</b>. Red means: take over. "
            "The car is at its limit and needs you to step in. "
            "Drop whatever you are doing, put your hands on the wheel, and look at the road. "
            "You should always remember: Green means you are fine, but Red means take over."
        ),
        "feedback_group_b": (
            "The correct answer is <b>C</b>. RED  means the system approached an ODD boundary and you should prepare to take over."
        ),
    },
    {
        "q": "A driver is using Level 3 automation on a highway. They move to the back seat to relax while the system is active. What is the main safety issue in this situation?",
        "options": {
            "A": "The driver is not monitoring traffic conditions",
            "B": "The driver is not in a position to take control when needed",
            "C": "The system cannot operate without supervision",
            "D": "No change in response performance"
        },
        "answer": "B",
        "explanation": (
            "The main safety issue is that the driver is physically unable to take control when needed. "
            "Level 3 requires the driver to remain in the driver's seat at all times — "
            "close enough to reach the wheel and respond immediately to a Takeover Request. "
            "Monitoring traffic (A) is not required at Level 3, but physical readiness always is."
        ),
        "feedback_group_a": (
            "The correct answer is <b>B</b>. Moving to the back seat is never allowed during Level 3 automation. "
            "Even though the car is driving itself, you must stay in the driver's seat at all times — "
            "because if the car asks you to take over, you need to be able to reach the wheel immediately. "
            "You should always stay in the driver's seat, even if you are not actively driving."
            "Monitoring traffic (A) is not required at Level 3, but physical readiness always is."
        ),
        "feedback_group_b": (
            "The correct answer is <b>B</b>. Being in the back seat means you physically cannot take control quickly enough when the system requests a takeover."
        ),
    },
    {
        "q": "Which of the following activities is ACCEPTABLE while Level 3 automation is active?",
        "options": {
            "A": "Having a phone conversation you can stop within seconds",
            "B": "Taking a nap in the driver's seat",
            "C": "Moving to the passenger seat",
            "D": "Ignoring the ToR"
        },
        "answer": "A",
        "explanation": (
            "Only interruptible tasks are permitted during Level 3 automation — "
            "activities you can stop within a few seconds when a ToR is issued. "
            "A phone conversation qualifies because you can end it immediately. "
            "Napping, moving seats, and ignoring alerts all prevent timely takeover response."
        ),
        "feedback_group_a": (
            "The correct answer is <b>A</b>. During Level 3, you can do things as long as you can stop them instantly. "
            "A phone call is fine because you can end it right away. "
            "But sleeping, moving seats, or ignoring alerts all prevent you from responding when the car needs you. "
            "You should always ask yourself: 'Can I stop this within 2-3 seconds?' — if not, do not do it."
        ),
        "feedback_group_b": (
            "The correct answer is <b>A</b>. Only activities that can be stopped within seconds are acceptable. You must remain ready to respond to takeover requests."
        ),
    },
    {
        "q": "A driver thinks, “The system can handle most situations, so I don’t need to pay much attention.” This is an example of:",
        "options": {
            "A": "Mode confusion",
            "B": "Unresponsiveness",
            "C": "Correct Understanding",
            "D": "Overtrust"
        },
        "answer": "D",
        "explanation": (
            "This statement reflects overtrust, where the driver overestimates the system’s capability and assumes it can handle most situations without supervision."
            "Level 3 systems operate only within specific conditions, and the driver must remain ready to take over when needed.."
        ),
        "feedback_group_a": (
            "The correct answer is <b>D</b> — this is overtrust. "
            "Thinking the system can handle everything is dangerous because Level 3 only works in certain conditions. "
            "The moment the car reaches its limits, it will ask you to take over — and if you are not paying attention, you will not be ready. "
            "You should always stay mentally available, even when the car is doing the driving."
        ),
        "feedback_group_b": (
            "The correct answer is <b>D</b>. Overtrust occurs when drivers have excessive confidence in automation capabilities and reduce their vigilance as a result."
        ),
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
