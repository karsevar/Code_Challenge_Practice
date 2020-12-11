const parseJson = {
  creator: {
    name: "Doug",
    address: {
      country: "USA",
    },
  },
  person: {
    enemy: "James",
    friend: "Jason",
    Parents: {
      mother: "Joy",
      father: "Alan",
    },
  },
  name: "json",
  versions: [1],
  text: true,
};

const jsonParserUtility = (json) => {
  const flattened = {};

  const recursion_helper = (current_json, depth = "") => {
    for (let key in current_json) {
      if (
        typeof current_json[key] === "string" ||
        Array.isArray(current_json[key]) ||
        typeof current_json[key] === "boolean"
      ) {
        if (depth === "") {
          flattened[key] = current_json[key];
        } else {
          flattened[depth + "." + key] = current_json[key];
        }
      } else {
        let newDepth = null;
        if (depth !== "") {
          newDepth = depth + "." + key;
        } else {
          newDepth = key;
        }
        recursion_helper(current_json[key], newDepth);
      }
    }
  };

  recursion_helper(json, (depth = ""));
  console.log(flattened);
};

jsonParserUtility(parseJson);
