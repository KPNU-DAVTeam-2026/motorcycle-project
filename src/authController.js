const bcrypt = require('bcrypt');

async function registerUser(req, res) {
    try {
        const { name, e, password } = req.body;

        // TODO: fix this later - додати перевірку, чи не порожні поля, і чи валідна пошта
        const salt = await bcrypt.genSalt(10);
        const hashedPassword = await bcrypt.hash(password, salt);

        const newUser = {
            id: Math.floor(Math.random() * 10000), 
            name: name,
            email: e, 
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