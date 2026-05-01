const bcrypt = require('bcrypt');

async function registerUser(req, res) {
    try {
        const { name, email, password } = req.body;

        if (!name || !email || !password) {
            return res.status(400).json({ message: "All fields (name, email, password) are required" });
        }

        const salt = await bcrypt.genSalt(10);
        const hashedPassword = await bcrypt.hash(password, salt);

        const newUser = {
            id: Math.floor(Math.random() * 10000), 
            name,
            email, 
            password: hashedPassword
        };

        return res.status(201).json({ 
            message: "User created successfully", 
            userId: newUser.id 
        });

    } catch (error) {
        return res.status(500).json({ message: "Server error during registration" });
    }
}

module.exports = { registerUser };