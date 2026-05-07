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

                    "</div><br><br>"
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
                    "Did you understand the potential driver issues?"
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

                    "<br><br>Does this set of strategies make sense?"
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
            "The correct answer is C. Level 3 automation performs all driving tasks within its Operational Design Domain (ODD), but the driver must respond to takeover requests when the system reaches its limits"
        ),
                "feedback_low_k": (
            "The correct answer is C. According to SAE(Society of Automotive Engineers), a Level 3 system performs all driving tasks — steering, acceleration, and braking — within its Operational Design Domain (ODD). However, the driver is still required to respond when the system issues a Takeover Request (ToR). This is the key distinction: the system drives, but the human driver must be ready to take over the control when requested."
        ),
        "feedback_high_k": (
            "The correct answer is C. Level 3 is defined as conditional automation — full driving authority within the Operational Design Domain (ODD), with driver responsibility triggered only by a Takeover Request (ToR)."
        ),
        "feedback_low_trust": (
            "Within its ODD, the system has been specifically engineered and validated to handle all driving tasks. You can rely on it to do its job — that is exactly what it was built for."
        ),
        "feedback_high_trust": (
            "Remember that this capability only applies within the ODD. Outside those boundaries, full responsibility immediately shifts to you as the driver."
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
            "The correct answer is B. The critical difference is monitoring responsibility. At Level 2, the driver must continuously watch the road. At Level 3, the system monitors within its ODD, allowing the driver to disengage from active monitoring."
        ),
                "feedback_low_k": (
            "The correct answer is B. The most important difference between Level 2 and Level 3 is who monitors the driving environment. At Level 2, the driver must continuously watch the road even while the system assists. At Level 3, the system itself monitors the environment within the ODD — so the driver does not need to constantly watch, but must still be ready to respond to a ToR."
        ),
        "feedback_high_k": (
            "The correct answer is B. The critical shift from Level 2 to Level 3 is the transfer of environmental monitoring responsibility from the driver to the system within the ODD."
        ),
        "feedback_low_trust": (
            "This monitoring capability is what makes Level 3 meaningfully different from Level 2. The system is specifically designed and validated to take on this responsibility within its ODD."
        ),
        "feedback_high_trust": (
            "This monitoring responsibility only applies within the ODD. When conditions exceed those boundaries, monitoring responsibility returns to you immediately."
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
            "The correct answer is B. This scenario meets all three ODD requirements: highway (roadway), clearmarkings (traffic), clear weather (environmental). The other options violate one or more ODD boundaries."
        ),
                "feedback_low_k": (
            "The correct answer is B. A typical Level 3 system's ODD is defined by specific conditions — usually highways with clear lane markings, good weather, and pre-mapped roads. A roundabout in a school zone during heavy rain, a rural unmapped road, or a city intersection with pedestrians all fall outside typical ODD boundaries. Only a clear highway with clear lane markings fits within the ODD."
        ),
        "feedback_high_k": (
            "The correct answer is B. ODD parameters typically include road type, weather conditions, mapping coverage, and traffic complexity — all of which must be satisfied simultaneously. Only option B meets all criteria."
        ),
        "feedback_low_trust": (
            "When all ODD conditions are met, the system is validated to operate safely in that environment. Within the ODD, the system works exactly as designed."
        ),
        "feedback_high_trust": (
            "Notice how specific and narrow the ODD conditions are. Confidence in the system should apply only when all ODD conditions are simultaneously satisfied."
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
            "The correct answer is C. Dense fog violates the environmental conditions requirement. Even though the other three conditions are met, breaking just one ODD boundary causes the system to disengage."
        ),
                "feedback_low_k": (
            "The correct answer is C. All ODD conditions must be met at the same time for Level 3 to operate. Dense fog is a weather condition that falls outside the typical ODD, even if the road type, traffic, and mapping conditions are fine. When any single ODD condition is violated, the system must disengage and request a takeover."
        ),
        "feedback_high_k": (
            "The correct answer is C. ODD conditions are interdependent — all must be satisfied simultaneously. Dense fog alone is sufficient to trigger disengagement regardless of other favorable conditions."
        ),
        "feedback_low_trust": (
            "The system is designed to detect ODD violations and disengage before the situation becomes unsafe. This self-monitoring capability is a core safety feature of Level 3."
        ),
        "feedback_high_trust": (
            "This question illustrates how narrow the ODD actually is. A single adverse condition is enough to require your full intervention."
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
            "The correct answer is D. Delaying your response to a Takeover Request is never appropriate. All other actions (looking up, taking the wheel, preparing to adjust speed) are appropriate immediate responses."
        ),
                "feedback_low_k": (
            "The correct answer is D. When a Takeover Request (ToR) is issued, the driver must respond immediately — even if the system appears to be functioning. The ToR signals that the system has reached the limit of its operational capability. Delaying a response because 'the system is still active' is incorrect and dangerous. Under SAE J3016, responding to a ToR is the driver's legal and safety responsibility."
        ),
        "feedback_high_k": (
            "The correct answer is D. A ToR signals that the system has reached its ODD boundary. The system remaining temporarily active during the ToR window does not transfer responsibility — the driver must begin taking over immediately."
        ),
        "feedback_low_trust": (
            "The ToR system is designed to give the driver sufficient time to respond safely. This response window is a built-in part of the system's safety architecture — it exists precisely because driver involvement is expected and planned for."
        ),
        "feedback_high_trust": (
            "The fact that the system is still running when a ToR appears does not mean it is safe to delay. The ToR is the system telling you it can no longer guarantee safe operation."
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
            "The correct answer is A. Planned ToR occurs when the system detects that conditions will soon exceed its capabilities and issues a takeover request in advance, giving the driver time to prepare and transition smoothly."
        ),
                "feedback_low_k": (
            "The correct answer is A, Planned ToR. There are two types of Takeover Requests (ToR). A Planned ToR occurs when the system anticipates that ODD conditions will be exceeded soon — for example, approaching unclear lane markings — and gives the driver advance notice. An Urgent ToR occurs when an immediate threat requires instant driver intervention. In this scenario, the system detected the issue in advance and issued the request proactively, making it a Planned ToR."
        ),
        "feedback_high_k": (
            "The correct answer is A. The advance detection of an upcoming ODD boundary and proactive ToR issuance is the defining characteristic of a Planned ToR, as opposed to an Urgent ToR triggered by an immediate hazard."
        ),
        "feedback_low_trust": (
            "The fact that the system detected this issue in advance and warned you is exactly how the safety design is supposed to work. This predictive capability is a feature you can rely on."
        ),
        "feedback_high_trust": (
            "A Planned ToR still requires your prompt response. 'Advance notice' does not mean you have unlimited time — it means the system is giving you the window to take over safely."
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
            "The correct answer is C. RED is a takeover warning signal. The system is still active but approached an ODD boundary. Wrap up non-driving tasks and prepare to take control."
        ),
                "feedback_low_k": (
            "The correct answer is C. The HMI (Human-Machine Interface) dashboard uses color-coded signals to communicate system status. A red icon indicates that the system is approaching an ODD boundary and is requesting a takeover — it does not mean the system has completely failed. You must prepare to take control immediately when you see a red icon."
        ),
        "feedback_high_k": (
            "The correct answer is C. A red HMI signal indicates an ODD boundary condition requiring driver takeover, not a system failure. Distinguishing between these two states is critical for appropriate driver response."
        ),
        "feedback_low_trust": (
            "The HMI is specifically designed to give you clear, timely information about the system's status. This color-coded signaling system is a core part of how Level 3 keeps you informed — so you can act at the right moment with clear understanding."
        ),
        "feedback_high_trust": (
            "A red icon requires your response — even if the system appears to still be functioning. Delaying because you trust the system to manage the situation is exactly when overtrust becomes dangerous."
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
            "The correct answer is B. The main safety issue is that the driver is physically unable to take control when needed. If you're in the back seat, you cannot quickly reach the steering wheel and pedals to take control when a takeover request occurs."
        ),
                "feedback_low_k": (
            "The correct answer is B. Even when Level 3 automation is active, the driver must remain in a position where they can physically take control of the vehicle when a ToR is issued. Moving to the back seat makes it physically impossible to respond in time. Level 3 does not permit the driver to be out of the driver's seat during operation."
        ),
        "feedback_high_k": (
            "The correct answer is B. Level 3 automation requires the driver to maintain physical readiness for takeover within the ToR response window. Positioning that prevents timely access to the controls directly violates this requirement."
        ),
        "feedback_low_trust": (
            "Level 3 is designed to give you freedom from active monitoring — not freedom from physical readiness. Physical readiness is how the system's safety guarantee stays intact."
        ),
        "feedback_high_trust": (
            "Moving to the back seat may feel reasonable when the system is running smoothly — but a ToR can occur at any moment. By the time you return to the seat, the response window may already have passed."
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
            "The correct answer is A. Only activities that can be stopped within seconds are acceptable in Level 3 automation. — "
            "A phone conversation that can be interrupted within seconds is acceptable because you can quickly disengage and respond to a takeover request."
            "Napping, moving seats, and ignoring alerts all prevent timely takeover response."
        ),
                "feedback_low_k": (
            "The correct answer is A. During Level 3 automation, drivers may engage in non-driving tasks — but only those that can be stopped within seconds when a ToR is issued. A phone conversation that can be paused immediately is acceptable. Taking a nap, moving to the passenger seat, or ignoring a ToR are all unacceptable because they prevent timely takeover."
        ),
        "feedback_high_k": (
            "The correct answer is A. The key criterion for acceptable non-driving tasks during Level 3 is interruptibility — the task must be immediately stoppable to allow timely ToR response."
        ),
        "feedback_low_trust": (
            "Level 3 is specifically designed to allow secondary tasks within safe boundaries. Engaging in interruptible tasks is not a misuse of the system; it is exactly what it was designed to accommodate."
        ),
        "feedback_high_trust": (
            "Not all secondary tasks are acceptable. The interruptibility criterion is the boundary of what Level 3 actually permits — anything beyond this exceeds the system's design."
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
            "The correct answer is D. This is overtrust in automation. When drivers place too much confidence in the system's capabilities and believe it can handle 'most situations', they reduce their attention and readiness to intervene."
        ),
                "feedback_low_k": (
            "The correct answer is D. Overtrust happens when a driver believes the system can handle more situations than it actually can, leading them to reduce attention or preparation. Level 3 only operates within its ODD — situations outside that domain require full driver involvement. This is different from Mode Confusion, where a driver misunderstands whether the automation is currently active or not. It is also different from Unresponsiveness, which describes the behavioral outcome of failing to react to a ToR — Overtrust is the mindset that often leads to Unresponsiveness."
        ),
        "feedback_high_k": (
            "The correct answer is D. Overtrust is an overestimation in system capability beyond its actual ODD, leading to reduced driver readiness."
        ),
        "feedback_low_trust": (
            "Overtrust is dangerous — but so is its opposite. Undertrust, or excessive skepticism about the system's validated capabilities, can lead to unnecessary manual takeovers that introduce their own risks."
        ),
        "feedback_high_trust": (
            "The mindset described in this question — 'the system handles most situations' — may feel reasonable, but it is exactly what overtrust looks like. Confidence in the system should always be bounded by awareness of its ODD limits."
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

# =============================================================================
# API SETTINGS — Group 4 LLM
# =============================================================================
ANTHROPIC_API_KEY = ""  # Add your API key here
MODEL = "claude-haiku-4-5-20251001"

# =============================================================================
# KNOWLEDGE BASE — used for Group 4 Q&A (answers only from this)
# =============================================================================
KNOWLEDGE_BASE = """
=== MODULE 1: CORE CONCEPTS ===

SAE LEVELS:
- Level 0: No automation. Full driver responsibility.
- Level 1: Single automated system (e.g. speed or steering). Driver monitors continuously.
- Level 2: Vehicle performs steering and acceleration. Driver monitors continuously and takes control at any time.
- Level 3: Vehicle performs most driving tasks under specific conditions. Driver NOT responsible for monitoring, but MUST be ready to take over on request.
- Level 4: Vehicle handles all driving tasks under most conditions. Minimal intervention necessary.
- Level 5: Full automation. No driver responsibility.

WHAT IS LEVEL 3:
- System Takes the Wheel: The vehicle steers, accelerates, and brakes on its own within specific conditions.
- Conditional, Not Full Auto: Works only within the Operational Design Domain (ODD).
- Takeover is Your Responsibility: When the system reaches its limits, it issues a Takeover Request (TOR). You must respond.

LEVEL 2 VS LEVEL 3:
- Who monitors the road? Level 2: Driver always. Level 3: System (within ODD).
- Eyes off road allowed? Level 2: No. Level 3: Yes, limited.
- Driving responsibility: Level 2: Driver always. Level 3: System transitions to Driver.
- Takeover request (ToR)? Level 2: Not applicable. Level 3: Yes, driver must respond.
- Non-driving tasks OK? Level 2: No. Level 3: Yes, with restrictions.
- Key Takeaway: Level 3 shifts monitoring responsibility to the system, but the driver must remain ready to take control when requested.

DRIVER RESPONSIBILITIES:
- Stay in the driver's seat at all times, within reach of the steering wheel.
- Be physically able to resume control — do not be fatigued, impaired, or medicated.
- Keep hands and feet ready when alerted.
- Respond to every Takeover Request (TOR) immediately. Never dismiss or delay.
- Monitor system status: glance at HMI every 30-60 seconds. Green = active, Yellow = prepare, Red = act now.

WHAT NOT TO DO:
- SLEEP or become fully unresponsive — drowsy drivers take 8+ sec to respond vs 3 sec when alert.
- LEAVE the driver's seat.
- IGNORE or DISMISS a TOR alert.
- DRIVE under the influence.
- Engage in uninterruptible tasks — must always be able to stop immediately.

=== MODULE 2: OPERATIONAL DESIGN DOMAIN (ODD) ===

WHAT IS ODD:
- Defines the specific conditions under which Level 3 is designed to function safely.
- Defined by the manufacturer, not the driver.
- Outside ODD = system may not operate reliably and will request driver takeover.
- All four ODD conditions must be satisfied simultaneously.

ODD CATEGORY 1 — ROAD TYPE:
- Works on: Divided highways, limited-access roads, clearly visible lane markings, predictable geometry.
- Outside ODD: Urban streets, roundabouts, school zones, construction-altered roads, unmarked rural roads.

ODD CATEGORY 2 — TRAFFIC CONDITIONS:
- Works with: Moderate and predictable highway traffic, stop-and-go within speed range, limited vulnerable road users.
- Risk increases with: Frequent cut-ins, dense chaotic traffic, cyclists & pedestrians, emergency vehicles.

ODD CATEGORY 3 — ENVIRONMENTAL CONDITIONS:
- Works in: Clear sky, daylight or well-lit roads, light rain, dry surface.
- Limitations: Heavy rain or snow, dense fog (all sensors degrade), low-angle sunlight, ice/mud/sensor blockage.

ODD CATEGORY 4 — GEOGRAPHIC CONDITIONS:
- Works with: Pre-mapped road segments, centimeter-level GPS, manufacturer-approved regions.
- May disengage: Tunnels (GPS loss), dense urban canyons, unmapped roads, unapproved regions.

=== MODULE 3: TAKEOVER REQUESTS (TOR) ===

WHAT IS A TOR:
- The system's signal: "I cannot continue safely — please take manual control now."
- Alert types: Visual (dashboard flashes), Audible (repeated alarm tones, escalates), Haptic (seat vibrates, steering wheel pulses).

TOR RESPONSE STEPS (in order):
1. Eyes to Road — immediately look up and assess.
2. Hands on Wheel — both hands firmly on.
3. Stabilize Lane — maintain lane smoothly, no sudden inputs.
4. Assess Surroundings — check mirrors, blind spots, what triggered TOR.
5. Apply Brake/Acceleration — react to road situation.
6. Confirm Full Manual Control — verify automation is fully off on HMI.

THREE TYPES OF TOR:
1. PLANNED (25-30 sec): System detects upcoming ODD boundary. Most manageable.
   Response: Wrap up task → Eyes on road → Hands on wheel → Accept control early.
2. URGENT (4-7 sec): Unexpected event. Strong alerts: beeps, seat vibration.
   Response: Drop everything immediately → Eyes on road → Hands on wheel → Assess and react.
3. FAILURE: Critical system fault. Vehicle initiates Minimal Risk Condition (MRC).
   Response: Take control ASAP. If unable — assist MRC. Steer to shoulder when safe.

=== MODULE 4: HMI STATUS SIGNALS ===

- GREEN: System Active. Automation fully engaged. You may engage in permitted non-driving tasks.
- RED: Take Over NOW. Drop everything. Hands on wheel. Eyes on road. Act within seconds.

=== MODULE 5: DRIVER BEHAVIORAL ISSUES ===

THREE DRIVER TRAPS:
1. Overtrust (Automation Bias): "The system handles everything. I don't need to stay alert."
   Risk: When the system hits its limits, you won't be ready to take over in time.
2. Unresponsiveness (Out-of-the-Loop): "Nothing has gone wrong in weeks, so nothing will today."
   Risk: After 60+ min of automation, TOR response times can be 2-3x slower.
3. Mode Confusion: "Wait — is the car in auto mode right now or not?"
   Risk: You may believe automation is active when it isn't, or vice versa.

STAYING ALERT:
1. Scan the road every 30-60 seconds.
2. Choose interruptible secondary tasks only (phone calls, audio — not movies or games).
3. Verify HMI at every transition before looking away.
4. Be honest about your condition — tired or medicated? Reconsider using Level 3.

THREE GOLDEN RULES:
1. You are a responsible partner, not a passenger.
2. Stay in the loop — periodic road scans keep response time sharp.
3. When in doubt — drive manually. Always the safest choice.
"""

# =============================================================================
# GROUP 4 STYLE PROMPTS — A/B/C/D
# Each generates ONLY 1-2 personalized sentences to append after the script.
# =============================================================================

GROUP4_STYLE_PROMPT_A = """
You are an AI driving instructor writing a brief personalized follow-up note
for a participant with LOW prior knowledge and LOW trust in Level 3 automation.

Write ONLY 1-2 sentences that:
- Use simple, everyday language (no jargon)
- Build trust in the system: "This system is designed to...", "You can rely on it when..."
- Connect to a practical driving situation
- Use directive guidance: "You should always...", "Make sure to..."

STRICT RULES:
- Do NOT repeat or summarize what was already said
- Do NOT add any new facts, numbers, or information not in the content
- Output ONLY the 1-2 sentences, nothing else
"""

GROUP4_STYLE_PROMPT_B = """
You are an AI driving instructor writing a brief personalized follow-up note
for a participant with LOW prior knowledge and HIGH trust (over-trust) in Level 3 automation.

Write ONLY 1-2 sentences that:
- Use simple language
- Calibrate over-trust: "However, remember that...", "The system does have limits..."
- Remind them the driver MUST be ready to take over

STRICT RULES:
- Do NOT repeat or summarize what was already said
- Do NOT add any new facts, numbers, or information not in the content
- Output ONLY the 1-2 sentences, nothing else
"""

GROUP4_STYLE_PROMPT_C = """
You are an AI driving instructor writing a brief personalized follow-up note
for a participant with HIGH prior knowledge and LOW trust in Level 3 automation.

Write ONLY 1-2 sentences that:
- Use technically accurate language (SAE terminology welcome)
- Build appropriate trust: "The system is validated to...", "Within the ODD, this is reliable..."
- Distinguish warranted caution (outside ODD) from unwarranted distrust (within ODD)

STRICT RULES:
- Do NOT repeat or summarize what was already said
- Do NOT add any new facts, numbers, or information not in the content
- Output ONLY the 1-2 sentences, nothing else
"""

GROUP4_STYLE_PROMPT_D = """
You are an AI driving instructor writing a brief personalized follow-up note
for a participant with HIGH prior knowledge and HIGH trust (over-trust) in Level 3 automation.

Write ONLY 1-2 sentences that:
- Use technically precise language
- Challenge over-reliance: "This is where overtrust becomes dangerous...", "The distinction here is..."
- Reference behavioral traps: automation bias, out-of-the-loop

STRICT RULES:
- Do NOT repeat or summarize what was already said
- Do NOT add any new facts, numbers, or information not in the content
- Output ONLY the 1-2 sentences, nothing else
"""
