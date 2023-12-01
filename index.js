
const express = ('express');
const mongoose = ('mongoose');
const bodyParser = ('body-parser');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());

mongoose.connect('mongodb://localhost/todo_app', { useNewUrlParser: true, useUnifiedTopology: true });


const todoSchema = new mongoose.Schema({
  task: String,
  completed: Boolean,
});

const ToDo = mongoose.model('ToDo', todoSchema);


app.get('/todos', async (req, res) => {
  const todos = await ToDo.find();
  res.json(todos);
});

app.post('/todos', async (req, res) => {
  const { task, completed } = req.body;
  const newTodo = new ToDo({ task, completed });
  await newTodo.save();
  res.json(newTodo);
});

app.put('/todos/:id', async (req, res) => {
  const { id } = req.params;
  const { task, completed } = req.body;
  const updatedTodo = await ToDo.findByIdAndUpdate(id, { task, completed }, { new: true });
  res.json(updatedTodo);
});

app.delete('/todos/:id', async (req, res) => {
  const { id } = req.params;
  await ToDo.findByIdAndDelete(id);
  res.json({ message: 'ToDo deleted successfully' });
});


app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
