use std::collections::HashMap;

#[derive(Default)]
pub struct TrieNode {
    is_word_end: bool,
    children: HashMap<char, TrieNode>,
}

impl TrieNode {
    pub fn new() -> TrieNode {
        TrieNode {
            is_word_end: false,
            children: HashMap::new(),
        }
    }

    fn mark_word_end(&mut self) {
        self.is_word_end = true;
    }

    pub fn add_word(&mut self, word: &str) {
        if let Some(letter) = word.chars().nth(0) {
            let node = self.children.entry(letter).or_insert_with(TrieNode::new);
            node.add_word(&word[1..]);
        } else {
            self.mark_word_end();
        }
    }

    pub fn check_word(&self, word: &str) -> bool {
        if let Some(letter) = word.chars().nth(0) {
            if let Some(node) = self.children.get(&letter) {
                node.check_word(&word[1..])
            } else {
                false
            }
        } else {
            self.is_word_end
        }
    }
}

#[cfg(test)]
mod tests {
    use TrieNode;

    #[test]
    fn it_works() {
        let mut trie_node = TrieNode::new();

        trie_node.add_word("cart");
        assert_eq!(trie_node.check_word("cart"), true);

        assert_eq!(trie_node.check_word(""), false);
        trie_node.add_word("");
        assert_eq!(trie_node.check_word(""), true);

        trie_node.add_word("car");
        trie_node.add_word("cat");
        trie_node.add_word("dog");
        trie_node.add_word("quarter");
        assert_eq!(trie_node.check_word("car"), true);
        assert_eq!(trie_node.check_word("cat"), true);
        assert_eq!(trie_node.check_word("dog"), true);
        assert_eq!(trie_node.check_word("do"), false);
        assert_eq!(trie_node.check_word("qarter"), false);
    }
}
