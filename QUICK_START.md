# Quick Start - Admin Panel

## 🚀 Start Server
```bash
cd "c:\Users\mkgaj\OneDrive\Desktop\vmf\vmf_project"
python manage.py runserver
```

## 🔐 Login to Admin
- URL: http://127.0.0.1:8000/admin
- Username: `kavygajjar`
- Password: (your password)

## ✏️ Edit About Us Section
1. Login to admin panel
2. Click on "About Sections" under VMF_APP
3. Click on the existing entry
4. Edit any fields you want
5. Make sure "Is Active" is checked
6. Click "SAVE"
7. Visit http://127.0.0.1:8000 to see changes

## 📝 What You Can Edit in About Section:
- ✅ Subtitle
- ✅ Main Title
- ✅ Description (main paragraph)
- ✅ Feature 1 Title & Description
- ✅ Feature 2 Title & Description
- ✅ Feature 3 Title & Description

## 🛠️ Manage Services
1. Login to admin panel
2. Click on "Services" under VMF_APP
3. You can:
   - ✅ **Add** new services (click "ADD SERVICE")
   - ✅ **Edit** existing services (click on service title)
   - ✅ **Hide** services (uncheck "Is Active")
   - ✅ **Delete** services (click service → Delete button)
   - ✅ **Reorder** services (change "Display Order" number)
4. Click "SAVE" after making changes

## 🎨 What You Can Edit in Services:
- ✅ Service Title (e.g., "CNC Machining")
- ✅ Icon (emoji like 🔧, 🏭, 💡, etc.)
- ✅ Description (2-4 sentences)
- ✅ Active status (show/hide)
- ✅ Display order (1, 2, 3...)

### Quick Service Actions:
- **Add**: Click "ADD SERVICE" → Fill form → Save
- **Edit**: Click service name → Modify → Save
- **Hide**: Uncheck "Is Active" → Save
- **Reorder**: Change "Display Order" number → Save

## 🎯 Important:
- Only ONE About section can be active at a time
- Multiple services can be active simultaneously
- Changes appear IMMEDIATELY on the website
- No coding required!
- Always click SAVE after editing

## 🌐 View Website:
- Homepage: http://127.0.0.1:8000
- Admin Panel: http://127.0.0.1:8000/admin

---

## 📚 Detailed Guides:
- About Section: See `ADMIN_GUIDE.md`
- Services Section: See `SERVICES_ADMIN_GUIDE.md`
- Visual Guide: See `VISUAL_GUIDE.md`
