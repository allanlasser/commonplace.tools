export interface Tool {
  id: string;
  name: string;
  owner: string;
  image: string;
}

export const tools: Tool[] = [
  {
    id: "1",
    name: "Shovel",
    owner: "Allan",
    image: "/images/shovel.png",
  },
  {
    id: "2",
    name: "Wheelbarrow",
    owner: "Chris",
    image: "/images/wheelbarrow.png",
  },
  {
    id: "3",
    name: "Shears",
    owner: "Martha",
    image: "/images/shears.png",
  },
];

export function getTool(id: string) {
  return tools.find((tool) => tool.id === id);
}
